"use strict";

var port = "5678";
if(document.domain)
  var wsurl = 'ws://' + document.domain + ':' + port;
else
  var wsurl = 'ws://localhost:' + port;
  // var wsurl = 'ws://192.168.1.122:' + port;
console.log("wsurl = " + wsurl);
var websocket = new WebSocket(wsurl);

var minus = document.getElementById('minus')
var plus  = document.getElementById('plus')
var value = document.getElementById('value')
var users = document.getElementById('users')

minus.onclick = function(event) {
  websocket.send(JSON.stringify({action: 'minus'}));
}

plus.onclick = function(event) {
  websocket.send(JSON.stringify({action: 'plus'}));
}

websocket.onmessage = function(event) {
  var data = JSON.parse(event.data);
  switch(data.type) {
    case 'state':
      if(data.value < 0)
        value.classList.add("negative");
      else
        value.classList.remove("negative");
      value.textContent = data.value;
      break;

    case 'users':
      users.textContent = (
        data.count.toString() + " user" +
        (data.count == 1 ? "" : "s"));
      break;

    default:
      console.error(
        "unsupported event", data);
  }
};
