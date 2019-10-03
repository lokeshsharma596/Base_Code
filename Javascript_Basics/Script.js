function alertpopup()
{
alert("Welcome");
}


function outputVars()
{
var score=90;
var age=5;

document.getElementById("lok").innerHTML= "Score:" +score +"Age:" +age + "<br/>";
}


function checkAge()
{
var age=4;
    if(age>18)
    {
        document.getElementById("lok").innerHTML= "Adult:Go to bar"+ "<br/>";
    }else
    {
        document.getElementById("lok").innerHTML= "Go to home and drink milk"+ "<br/>"; 
    }
}



function checkZip()
{
    var zip="201303";
    var city;
    switch(zip)
    {
        case "201301":
            town="Noida"
            break;
        case "201303":
            town="SEZ"
            break;
        case "334001":
            town="Bikaner"
    }
    document.getElementById("lok").innerHTML="Town is" + town + "<br/>";
}



function printno()
{
    var a=20;
    while(a<28){
        document.getElementById("lok").innerHTML += a + "<br/>";
        a++;
    }
}

function printnodw()
{

        var n=20;
        do{
            document.getElementById("lok").innerHTML += n + "<br/>";
            n+=10;

        }while(n<100);

}

function printex()
{

    for (i=0;i<100;i+=5)
    {
        document.getElementById("lok").innerHTML += i + "<br/>";  
    }
}


function arraypri()
{
    var name=new Array();
    name[0] = "The";
    name[1] = "kesh";
    name[2] = "ok";
    name[3] = "sh";
    name[4] = "Lo";


    var family = new Array("Lokesh","Ravi","praveen","jiu");

    var states =["Raj","Guj","Maharastra"];

   
    document.getElementById("lok").innerHTML= name[0] + "<br/>" + family[1] + "<br/>" + states[2] + "<br/>";


    for(var i=0;i<name.length;i++)
    {
        document.getElementById("lok").innerHTML += name[i] + "<br/>" ;
    }
    
}