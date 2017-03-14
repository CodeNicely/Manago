var modal = document.getElementById('myModal');
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
var chkbtn=document.getElementById("btn");



$("#myBtn").on('click', function() {
$('#fileinput').val("");
$('#info').val("");
    modal.style.display = "block";

});


function validateForm(){
var y=document.getElementById("fileinput");
var text=document.getElementById("info").value;
var hdng=document.getElementById("caption").value;
if(hdng=="")
{
	if(y=="")
	{
		alert("Heading or file attachment is compulsory");
		return false;
	}
	else
	{
	y=y.split('.').pop();
	y=String(y).toLowerCase();
	if(y=="jpg"||y=="jpeg"||y=="png")
		{alert("Image");return true;}
	else if(y=="mp4"||y=="gif")
		{alert("video");return true;}
	else if(y=="apk")
		{alert("apk");return true;}
    else {
    	alert("Uploaded file format not supported");
    	return false;
    }
	}
}
else return true;
}

span.onclick = function() {
    modal.style.display = "none";
}


window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
