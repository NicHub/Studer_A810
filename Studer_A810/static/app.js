"use strict";

var connection;
openWebSocket();

function openWebSocket() {
  var wsurl = 'ws://' + location.hostname + ':' + location.port;
  console.log(wsurl);
  try {
    connection = new WebSocket( wsurl );
  } catch( exception ) {
    console.error( exception );
  }
}
