const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
setTimeout(function(){
    $('#messages').fadeout(slow);
},300);