function validateform1(){
    var job=document.getElementById('job').value
    var quali=document.getElementById('quali').value
    var exp=document.getElementById('exp').value
    var places=document.getElementById('places').value
    var skills=document.getElementById('skills').value
    if(job==""||quali==""||exp==""||skills==""){
        document.getElementById('error1').innerHTML="All fields must be filled out"
        return false
       }
    else
    {
        return true
    }  
}