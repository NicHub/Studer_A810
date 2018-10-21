#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
sudo pip3 install pyyaml
"""

import asyncio
from threading import Thread
import serial
import time
import yaml
import sys

if sys.platform == "linux":
    ports = ["/dev/ttyACM0"]
elif sys.platform == "darwin":
    ports = ["/dev/cu.usbmodem1421"]
else:
    print("Unsuported OS")
    sys.exit(0)

baud = 115200


# %%
class threaded_serial(Thread):
    """

    """
    toggle_index = 0
    def __init__(self, port, thread_index):
        Thread.__init__(self)
        self.thread_index = thread_index
        self.serial_port = serial.Serial(port, baud, timeout=0)

    def run(self):
        self.read_from_port(self.serial_port, self.thread_index)

    def read_from_port(self, ser, thread_index):
        while True:
            data = ser.readline().decode("unicode_escape")
            if len(data) > 0:
                try:
                    infos = yaml.load(data)
                    if isinstance(infos, dict):
                        try:
                            for key, value in infos.items():
                                print("Thread = {} - {} = {}".format(thread_index, key, value))
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
                time.sleep(0.1)
                self.toggle_index = self.toggle_index % 4 + 1
                ser.write("{}\n".format(self.toggle_index).encode("utf-8"))

        ser.close()


# %%
async def main():
    print("Threaded serial start")

    serial_threads = []

    for thread_index, port in enumerate(ports):
        serial_threads.append(threaded_serial(port, thread_index))

    for serial_thread in serial_threads:
        serial_thread.start()

    for serial_thread in serial_threads:
        serial_thread.join()

# %%
def test():
    print("Threaded serial start")

# %%
if __name__ == "__main__":
    main()


main()
