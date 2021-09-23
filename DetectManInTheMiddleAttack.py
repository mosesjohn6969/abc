# imports
import os
import time

import ipaddress
import struct

from uuid import getnode as get_mac
from subprocess import Popen, PIPE
import re
import socket
import csv
import subprocess
import sys

# external imports (had to download the package first)
from IPy import IP


# method to get the ARP table for an ip
def get_arp_table(IP):
    cmd = "arp -a"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    interfaceBocks = output[0].split("Interface:")

    for interfaceBock in interfaceBocks:
        lines = interfaceBock.split('\r\n')
        interfaceIP = lines[0].split('---')[0].strip()

        if interfaceIP == IP:
            names = ['Internet Address', "physical Address", "Type"]
            reader = csv.DictReader(lines[1:], fieldnames=names, skipinitialspace=True, delimiter=' ')
            next(reader)
            return [block for block in reader]

# method to get an ip address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


# start
def start():
    # calling the get ip method
    IP = get_ip()

    arp_table = get_arp_table()