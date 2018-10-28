"use strict";

var port = "5678";
var force_localhost = true;

if(document.domain && ! force_localhost)
  var wsurl = "ws://" + document.domain + ":" + port;
else
  var wsurl = "ws://localhost:" + port;
console.log("wsurl = " + wsurl);

var ws = null;


/* ******
  Check communication speed at regular intervals.
**** */
setInterval(check_ws_speed_send, 1000);
var tic, toc;

function check_ws_speed_send() {
  var mytime = new Date();
  tic = mytime.getMilliseconds();
  ws.send(JSON.stringify({action: "check_ws_speed"}));
}

function check_ws_speed_receive(data) {
  var mytime = new Date();
  toc = mytime.getMilliseconds() - tic;
  id_wsspeed.textContent = "time elapsed: " + toc + " ms";
}


/* ******
  Events triggered by the user on the web page.
**** */
id_minus.onclick = function(event) {
  ws.send(JSON.stringify({action: "minus"}));
}

id_plus.onclick = function(event) {
  ws.send(JSON.stringify({action: "plus"}));
}


/* ******
  Events triggered by the remote websocket server.
**** */
function state(data) {
  if(data.value < 0)
    id_value.classList.add("negative");
  else
    id_value.classList.remove("negative");
  id_value.textContent = data.value;
}

function users(data) {
  id_users.textContent = (
    data.count.toString() + " user" +
    (data.count == 1 ? "" : "s") +
    " online" );
}


/* ******
  Websocket handling.
**** */
function start() {
  console.log("Connecting websocket at " + wsurl);
  ws = new WebSocket(wsurl);

  ws.onopen = function() {
    console.log("connected!");
  };

  ws.onmessage = function(event) {
    // console.log(event.data);
    var data = JSON.parse(event.data);
    try {
      window[data.type](data);
    } catch(e) {
      console.error("Unsupported event", data);
    }
  };

  ws.onclose = function() {
    id_users.textContent = ("Connection closed");
    setTimeout(check_websocket, 1000);
  };
}

function check_websocket() {
  if(!ws) {
    console.log("--- STARTING ---");
    start();
    return;
  }
  if(ws.readyState == WebSocket.CONNECTING) {
    console.log("ws.readyState = CONNECTING");
  }
  else if(ws.readyState == WebSocket.OPEN) {
    console.log("ws.readyState = OPEN");
  }
  else if(ws.readyState == WebSocket.CLOSING) {
    console.log("ws.readyState = CLOSING");
  }
  else if(ws.readyState == WebSocket.CLOSED) {
    console.log("ws.readyState = CLOSED");
    start();
  }
}

check_websocket();
