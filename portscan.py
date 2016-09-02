#!/usr/bin/env python3
# portscan.py - a simple portscanner project to practice network programming
# in python3

import socket

# get the IP address of the host to scan
host = input("Enter the name of the host to scan: ")
hostIP = socket.gethostbyname(host)

# get the range of ports to scan

# create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the socket

# return results based on the return value