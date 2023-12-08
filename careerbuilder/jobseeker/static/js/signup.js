
function validateform()
{
var name=document.getElementById("name").value
var dob=document.getElementById("dob").value
var email=document.getElementById("email").value
var mb=document.getElementById("mb").value
var p1=document.getElementById("p1").value
var p2=document.getElementById("p2").value
if(name==""||dob==""||mb==""||email==""||p1==""||p2=="")
{
document.getElementById('error1').innerHTML="All fields must be filled out"
return false
}
else if(p1.length<6){
document.getElementById('error1').innerHTML="Password must be atleast 6 characters"
return false
}
else if(p1!==p2)
{
document.getElementById('error1').innerHTML="Password must be same"
return false
}
}