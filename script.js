var text = localStorage.getItem("data");
var obj = JSON.parse(text);


function click(arg){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            data = JSON.parse(this.responseText);
            document.getElementById("some").innerHTML = data[arg]["name"];
        }
    };
    xhttp.open("GET","data.json",true);
    xhttp.send();
	
}
