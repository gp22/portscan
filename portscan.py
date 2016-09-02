#!/usr/bin/env python3
# portscan.py - a simple portscanner project to practice network programming
# in python3

import argparse
import socket
import time

parser = argparse.ArgumentParser(description='scan for open TCP/IP ports')
parser.add_argument('host', 
                    help='name or IP of the host to scan')
parser.add_argument('-r', '--range', nargs=2, type=int, 
                    help='port range to scan: [start port] [end port]')
args = parser.parse_args()

host = args.host
port_range = args.range

# get the IP address of the host to scan
hostIP = socket.gethostbyname(host)

print('-' * 60)
print('Please wait, scanning {} at {}'.format(host, hostIP).center(60))
print('-' * 60, '\n')

# get the starting time
start_time = time.monotonic()

for p in range(port_range[0], port_range[1] + 1):
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