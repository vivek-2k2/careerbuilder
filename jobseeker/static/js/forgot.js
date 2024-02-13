function validateform()
{
    var email=document.getElementById("email").value
    if(email=="")
    {
        document.getElementById('error1').innerHTML='Please enter a valid input'
        return false
    }
}