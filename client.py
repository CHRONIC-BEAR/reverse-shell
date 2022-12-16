#client.py >> will later turn this into an exe file for Windows
#This program will be put on the client system, that when executed, sends data to my server that I can see
import socket

SERVER_IP = '192.168.1.79'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT)) #self explanatory I think...
    #once connected, the first thing that happens is the server sends the message
    data = s.recv(1024) #s.recv is the function that will receive that message, we can store it in a variable called data
    #the argument s.recv() takes is the buffer_size, how many bytes need to come in before it starts processing/executing all the code below it
    print(data) #print the message to the screen

input() #Just so the message will stay on the screen instead of closing out
