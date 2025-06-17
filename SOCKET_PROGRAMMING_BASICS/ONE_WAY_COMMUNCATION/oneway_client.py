import socket

HOST = "127.0.0.1" 
PORT = 12345 

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cs.connect((HOST,PORT))
    message = input("Type message: ")
    cs.sendall(message.encode()) #sendall ensures all data is send
    print(f"Client sent: '{message}'")
    
except socket.error as e:
    print(f"Connection error: {e}")
finally:
    cs.close() #always close the socket
