#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# WS server that sends messages at random intervals
# https://websockets.readthedocs.io/en/stable/intro.html
# pip install websockets

import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()