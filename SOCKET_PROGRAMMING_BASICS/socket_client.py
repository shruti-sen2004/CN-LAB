import socket

SERVER_HOST = "127.0.0.1" # local address for common testing
SERVER_PORT = 12345 

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    cs.connect((SERVER_HOST, SERVER_PORT))
    print(f"Client connected to {SERVER_HOST}:{SERVER_PORT}")

    msg = "Hello one way message from client is here"
    cs.send(msg.encode("utf-8")) #TCP is byte oriented cannot directly send string
except socket.error as e:
    print(f"Connection error: {e}")