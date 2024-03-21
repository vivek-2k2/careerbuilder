function validateform()
{
    var no=document.getElementById("no").value
    var expd=document.getElementById("expd").value
    var cvv=document.getElementById("cvv").value
    var name=document.getElementById("name").value
        if(no==""||expd==""||cvv==""||name=="")
    {
        document.getElementById('error1').innerHTML="All fields must be filled out"
        return false
    }
    else
    {
        return true
    }  
}