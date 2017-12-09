function onWindowLoad() {
    //document.getElementById("button1").addEventListener("click",sendKeywords2);
	console.log("updateScr");
}

function sendKeywords2()
{
	var query = document.keywordform.searchQ.value.toString();
    console.log("qe: "+ query);
    var newLoc = "query/"+query;
    console.log(newLoc);
    window.location=newLoc;

    return false;
}
window.onload = onWindowLoad;


