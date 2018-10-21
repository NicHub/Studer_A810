#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

import sys
from threading import Lock
from oui_serial.list_serial_ports import list_serial_ports


import asyncio
import datetime
import random
import websockets


async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)


if __name__ == '__main__':
    print("STARTING WEBSOCKET")
    start_server = websockets.serve(time, '0.0.0.0', 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    socketio.run(app, host='0.0.0.0', debug=True)
