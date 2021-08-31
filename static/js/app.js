
// convert json array into Table Structure
function makeTable(array) {
    // List of desired attributes
    arr_cols = ['name','deck','api_detail_url']
    // create a table element and assign an id
    var table = document.createElement('table');
    table.setAttribute("id","results_table");
    // loop through the results set and get the desired attributes
    // Add them as a row to table
    for (var i = 0; i < array.length; i++) {        
        var row = document.createElement('tr');
        for(itr in array[i]){
            var cell = document.createElement('td');
            if(arr_cols.includes(itr)){
                cell.textContent = array[i][itr];
                row.appendChild(cell);
            }
        }
        table.appendChild(row);
    }
    return table;
}

// Function to take user input and search
// Submit AJAX request to get data from Giantbomb API
// If Successfull then display the results on to the page
function fn_search(){
    // Get user input by ID
    var inputString = document.getElementById("id-input-str").value
    console.log(inputString)
    // Submit AJAX request to server
    var request = $.ajax({
        url: "/search",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(inputString),
        // AJAX request successful   
        success: function (response) {
            // Modify DOM to add table with results
            table_data = makeTable(response)
            document.getElementById('results_data').innerText = "";
            document.getElementById('results_data').innerHTML = '<table class="table table-bordered table-responsive table-striped"> ' + table_data.innerHTML + "</table>";
        },
        error: function (response) {
        }   
    })
    console.log("Complete")

}