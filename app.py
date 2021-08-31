#Import Dependencies
from flask import Flask, url_for, render_template, request, jsonify
import os
import api_keys as apikey
import requests
import json

# Create Flask Instance
app = Flask(__name__)

# Route for index page
@app.route('/')
def index():
    # Return Home Page 
    return render_template('base.html')

# Route for post requests for search
@app.route('/search',methods=['POST'])
def search_post():    
    data = request.get_json()
    # Creating header for user agent, required for API to authenticate along with API key   
    ua_headers={'user-agent':'ananyay'}
    api_url_pre = 'https://www.giantbomb.com/api/search/?api_key='
    # API key
    api_url_key = apikey.api_key_ay
    api_url_mid = '&format=json&query="'
    api_url_srch = data
    api_url_suf = '"&resources=game'
    # API URL
    api_url_req = api_url_pre + api_url_key + api_url_mid + api_url_srch + api_url_suf
    print(api_url_req)
    # Submit API requests
    uResponse = requests.get(api_url_req, headers=ua_headers)
    data = json.loads(uResponse.content)
    # Filter to only select the results attribute
    results = data['results'] 
    # Return JSON array 
    return jsonify(results)

# Route for GET requests for search
@app.route('/search',methods=['GET'])
def search_get():
    print("In the search get route")
    return render_template('search.html',row_data ="")

#  API Endpoint for curl 
@app.route('/search/<inputstr>')
def search_enpoint(inputstr):
    ua_headers={'user-agent':'ananyay'}
    api_url_pre = 'https://www.giantbomb.com/api/search/?api_key='
    api_url_key = apikey.api_key_ay
    api_url_mid = '&format=json&query="'
    api_url_srch = inputstr
    api_url_suf = '"&resources=game'
    api_url_req = api_url_pre + api_url_key + api_url_mid + api_url_srch + api_url_suf
    print(api_url_req)
    uResponse = requests.get(api_url_req, headers=ua_headers)
    data = json.loads(uResponse.content)
    results = data['results'] 
    return jsonify(results)

if __name__ == "__main__":
    app.run()