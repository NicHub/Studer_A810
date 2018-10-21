#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""
from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import sys
sys.path.append('/home/pi/Studer_A810/rpi_rs232')
from list_serial_ports import list_serial_ports


def main():
    """
    """

    [available_serial_ports, unavailable_serial_ports] = list_serial_ports()

    print("\nAVAILABLE_SERIAL_PORTS")
    for sp in available_serial_ports:
        print(sp)

    print("\nUNAVAILABLE_SERIAL_PORTS")
    for sp in unavailable_serial_ports:
        print(sp)



if __name__ == '__main__':
    main()
