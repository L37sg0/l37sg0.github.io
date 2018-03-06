function set_article(arg){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            data = JSON.parse(this.responseText);
            document.getElementById("tit").innerHTML = data[arg]["name"];
            document.getElementById("txt").innerHTML = data[arg]["text"];
            document.getElementById("image").setAttribute("src", data[arg]["image"]);
        }
    }
    xhttp.open("GET","data.json",true);
    xhttp.send();
	
}
