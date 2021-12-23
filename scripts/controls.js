function changecontent(){
    var row = prompt("Enter row number");
    var col = prompt("Enter column number");
    var string = prompt("Enter new content for cell");

    table = document.getElementById("myTable")

    var row2 = row - 1
    var col2 = col - 1

    for (var i = 0, r; r = table.rows[i]; i++){
        for (var j = 0, c; c = r.cells[j]; j++){

            //console.log("row: " + row2 +"col: " + col2 + "i: " + i+ "j: " + j)
            if (row2 == i && col2 == j){
                //console.log("row: " + i +"col: " + j);
                c.innerHTML = string;
            }
        }
    }
}