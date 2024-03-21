
function validateform1()
{
   
    
var name=document.getElementById('name').value

var dob=document.getElementById('dob').value


var mob=document.getElementById('mob').value

var email=document.getElementById('email').value

var quali=document.getElementById('quali').value
var cv=document.getElementById('cv').value

if(name==""||dob==""||mob==""||email==""||quali==""||cv=="")
{
document.getElementById('error1').innerHTML="All fields must be filled out"
return false
}
else{
    return true
}
}