#server.py
#This program will be running continuously on my local malicious server
import socket #Module that supports socket programming

#Server
SERVER_IP = '192.168.1.79' #IP of the malicious server
SERVER_PORT = 5678 #Port where the server will connect to the client (Can be any number between 1 - 65536)

#Socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #We are accessing the socket module, and inside is the socket function that returns a socket object
#socket.socket takes arguments... (address_family, type)
#AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with (in this case Internet Protocol v4 addresses)
#SOCK_STREAM is the transport protocol the socket will use, which is TCP, while SOCK_DGRAM is UDP
#the "as" keyword means alias, it assigned the socket object the alias s, (ea) import random as geek
#well, only jeezus knoes
    #we need to bind the server_ip and server_port to this socket
    s.bind((SERVER_IP, SERVER_PORT)) #binds the server_ip and server_port to the s socket
    #the bind() method in python's socket class assigns an IP address and a port number to a socket instance
    #bind takes the arguments in a tuple form as (('ip_address',port_number))
    #a server socket is required to be assigned a port and an IP address, although the kernel of the OS will assign the source IP and a temporary port number to the client socket
    print('Server listening...') #so we know the program is running
    s.listen(1) #listen() determines how many connections our socket can handle, in this case we will set it to 1
    #when this code is run, it stops at the above line, and won't execute anything below it until it gets a connection
    conn, addr = s.accept()
    #once a connection comes in from a client, it will run the s.accept() function which will return 2 things
    #the s.accept() function returns an object that represents the connection between the server and the client (conn)
    #and it returns a variable that stores connected client's address (addr)
    #now we will use the connection object to send data back and forth between the server and client
    print(f'Connection established from: {addr}') #so we know when the server has received a connection
    with conn: #apparently the conn works the same way as a file object, and you need to close it out
        while True: #we want to create a loop that sends and receives data over and over again
            conn.send(b'hello world') #the connection object has a function called send(), in which you can send data to the connected client
            #whenver sending data over a socket, it always has to be binary
            break #close the program
