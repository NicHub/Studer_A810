#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

import serial.tools.list_ports
import sys


# %%
def list_serial_ports():
    """
    Lists serial ports

    :returns:
        - A list of available serial ports, i.e. the ports that can be opened.
        - A list of unavailable serial ports, i.e. the ports that cannot be opened.
    """
    if sys.platform == "linux":
        serial_ports = serial.tools.list_ports.grep("/dev/(?!ttyAMA0)")
    elif sys.platform == "darwin":
        serial_ports = serial.tools.list_ports.grep("/dev/(?!cu.Bluetooth-Incoming-Port)")
    elif sys.platform == "win32":
        serial_ports = serial.tools.list_ports
    else:
        print("Unsupported OS")
        return [[],[]]

    available_serial_ports = []
    unavailable_serial_ports = []
    for serial_port in serial_ports:
        try:
            ser = serial.Serial(serial_port[0], 115200, timeout=1)
            if ser.is_open:
                available_serial_ports.append(serial_port[0])
            else:
                unavailable_serial_ports.append(serial_port[0])
        except Exception as e:
            unavailable_serial_ports.append(serial_port[0])
        else:
            pass
        finally:
            pass

    return [sorted(available_serial_ports),
            sorted(unavailable_serial_ports)]


# %%
if __name__ == "__main__":

    [available_serial_ports, unavailable_serial_ports] = list_serial_ports()

    print("\nAVAILABLE_SERIAL_PORTS")
    for sp in available_serial_ports:
        print(sp)

    print("\nUNAVAILABLE_SERIAL_PORTS")
    for sp in unavailable_serial_ports:
        print(sp)

