import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 2566

client_socket.connect((host, port))

while True:
    message = input("Type message: ")
    client_socket.sendall(message.encode()) # ensures all messages are sent 
    if message.lower() == 'exit':
        break
    
    data = client_socket.recv(1024).decode() # receives and decodes response from server 
    print("Received from server: ", data)

client_socket.close()