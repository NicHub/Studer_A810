#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
# import oui_serial.threaded_serial as threaded_serial

logging.basicConfig()

STATE = {'value': 0}

USERS = set()

def state_event():
    return json.dumps({'type': 'state', **STATE})

def users_event():
    return json.dumps({'type': 'users', 'count': len(USERS)})

async def notify_state():
    if USERS:
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def notify_users():
    if USERS:
        message = users_event()
        print(message)
        await asyncio.wait([user.send(message) for user in USERS])

async def notify_check_ws_speed(websocket):
    if USERS:
        message = json.dumps({"type": "check_ws_speed_receive", "value": 0})
        await asyncio.wait([websocket.send(message)])

async def register(websocket):
    USERS.add(websocket)
    await notify_users()

async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()

async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data['action'] == 'minus':
                STATE['value'] -= 1
                print("value = {}".format(STATE['value']))
                await notify_state()
            elif data['action'] == 'plus':
                STATE['value'] += 1
                print("value = {}".format(STATE['value']))
                await notify_state()
            elif data['action'] == 'check_ws_speed':
                await notify_check_ws_speed(websocket)
            else:
                logging.error(f"unsupported event: {data}")

    finally:
        await unregister(websocket)

def main():

    print("STARTING WEBSOCKET")
    print(f"websockets.__version__ = {websockets.__version__}")

    start_server = websockets.serve(counter, '0.0.0.0', 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        print("\b\b\033[K")
        print("\nThat’s all folks")
