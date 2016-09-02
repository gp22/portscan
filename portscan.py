#!/usr/bin/env python3
# portscan.py - a simple portscanner project to practice network programming
# in python3

import socket
import time

# get the IP address of the host to scan
host = input("Enter the name of the host to scan: ")
#host = 'vulnerable'
hostIP = socket.gethostbyname(host)

# get the range of ports to scan
port = 12

print('-' * 60)
print('Please wait, scanning {} at {}'.format(host, hostIP).center(60))
print('-' * 60, '\n')

# get the starting time
start_time = time.monotonic()

for p in range(1, 1025):
    # create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    # try to connect the socket at specified port    
    connect_result = sock.connect_ex((hostIP, p))
    if connect_result == 0:
        print('Port {}: Open'.format(p))
    sock.close()

# get the ending time
end_time = time.monotonic()

# print results
duration = end_time - start_time
duration = round(duration, 2)
print('\nN ports scanned in {} seconds'.format(duration))