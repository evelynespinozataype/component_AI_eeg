//const socket = io.connect('//' + document.domain + ':' + location.port + '/index');
//const socket = io()

let output = document.getElementById('output');

socket.on('message', data =>{
    console.log("DATOS: ",data);
    /*output.innerHTML = ~´<p>
    
    </p>´*/
});