import socket

HOST = "127.0.0.1" # local address for common testing
PORT = 12345 
# Create a socket object
# AF_INET -> IPV4
# SOCK_STEAM -> TCP
# SOCK_DGRAM -> UDP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")

s.bind((HOST,PORT))
print(f"Server bound to {HOST}:{PORT}")

s.listen(5)
print("Server is listening")
