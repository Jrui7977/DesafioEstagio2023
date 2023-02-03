let saida = "<h2><center>Clientes cadastrados : </center></h2>";
fetch('https://randomuser.me/api/?results=50')

    .then(res => res.json())
    .then(data => {

        let client = data.results;

        client.forEach(function (lists) {

        saida += `<div class = "client-content-info" style = 

        "
        display : flex;
        flex-direction : row;
        margin-top : 10%;
        border : 1px solid gray;
        border-radius : 5px;
        background-color : #0086ff;
        color : white;"
        > 
        <div class = "client-content-img">
        <img src = "${lists.picture.large}" style = "border : 2px solid #0086ff; border-radius : 15px;">
        </div>

        <div class = "client-content-data" style = 
        "display : flex;
        flex-direction : column;
        justify-content : center;
        list-style:none;
        
        ">
        
        <li>Nome : ${lists.name.first}${lists.name.last}</li>
        <li>Email : ${lists.email}</li>
        <li>Idade : ${lists.registered.age}</li>
        <li>Cidade : ${lists.location.city}</li>
        
        
        </div>
        </div>
        `
        document.getElementById('client-content').innerHTML = saida;
        });
    })


