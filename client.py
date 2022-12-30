#this program will be put on the client system, that when executed, takes data received from the server, and prints it to the screen
#these programs are very simple in nature, and were mainly developed to show the basic logic of a reverse shell
import socket

SERVER_IP = '' #enter IP of the listening device (server)
SERVER_PORT = 5678 #can be any port that is not being used..

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT)) #the connect function takes the server IP and the port the server is listening on as arguments
    #once connected, the server sends a message
    
    data = s.recv(1024) #s.recv is the function that will receive that message, we can store it in a variable called data
    #the argument s.recv() takes is the buffer_size, how many bytes need to come in before it starts processing/executing the code below it
    
    print(data) #print the message to the screen

input() #so the message will stay on the screen instead of closing out
