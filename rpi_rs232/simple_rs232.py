#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import serial
from time import sleep
import glob
import yaml


# %%
def findSerialPort():
    """

    """
    USB_PATTERNS = [
      "/dev/cu.usb*",
      "/dev/ttyACM*"
    ]

    ans = []
    for usb_pattern in USB_PATTERNS:
        ans = glob.glob(usb_pattern)
        if len(ans) > 0:
            break

    if len(ans) > 0:
        print("Serial port found : {}\n".format(ans[0]))
        return ans[0]
    else:
        print("No serial port found")
        return ""


# %%
def main(serial_port):
    """

    """
    ser = serial.Serial(serial_port, 115000, timeout=0)

    ser.write("1".encode("utf-8"))

    while True:
        data = ser.read(9999).decode('unicode_escape')
        if len(data) > 0:
            try:
                infos = yaml.load(data)
                if isinstance(infos, dict):
                    try:
                        for key, value in infos.iteritems():
                            print("{} = {}".format(key, value))
                        print("\n")
                        # if "TEMPERATURE_C" in infos:
                        #     print("TEMPERATURE_C = {}".format(infos["TEMPERATURE_C"]))
                        # if "LIGHT_METER" in infos:
                        #     print("LIGHT_METER = {}".format(infos["LIGHT_METER"]))
                        # if "LIGHT_METER" in infos:
                        #     print("LIGHT_METER = {}".format(infos["LIGHT_METER"]))
                        # if "LIGHT_METER" in infos:
                        #     print("LIGHT_METER = {}".format(infos["LIGHT_METER"]))
                        # if "LIGHT_METER" in infos:
                        #     print("LIGHT_METER = {}".format(infos["LIGHT_METER"]))
                    except yaml.YAMLError as exc:
                        pass
            except yaml.YAMLError as exc:
                pass
        else:
            sleep(0.1)

    ser.close()


# %%
if __name__ == "__main__":
    """

    """
    serial_port = findSerialPort()
    if not serial_port == "":
        main(serial_port)

