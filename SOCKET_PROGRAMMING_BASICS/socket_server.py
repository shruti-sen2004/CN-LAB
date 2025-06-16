import socket

HOST = "127.0.0.1" # local address for common testing
PORT = 12345 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")

s.bind((HOST,PORT))
print(f"Server bound to {HOST}:{PORT}")

s.listen(5)
print("Server is listening")

conn, addr = s.accept() # socket specifically used for this communication only
print(f"Accepted connection from {addr}")

# it can also have a send function but for now we are only taking the receive function

# when receiving the encoded msg
data = conn.recv(1024) # 1024 -> max amount of data in bytes
if data:
    decoded_msg= data.decode("utf-8")
    print(f"Server received: {decoded_msg} from {addr}")