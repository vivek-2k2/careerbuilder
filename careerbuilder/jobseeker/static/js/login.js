function validateform()
{
    var email=document.getElementById("email").value
    var p1=document.getElementById("p1").value
    if(email==""||p1=="")
    {
        document.getElementById('error1').innerHTML="All fields must be filled out"
        return false
    }
    else
    {
        return true
    }
    
}