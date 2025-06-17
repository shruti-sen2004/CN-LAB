import socket

HOST = "127.0.0.1" 
PORT = 12345 

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((HOST,PORT))
ss.listen(3) # Listens to only one connection at a time
print(f"Server is listening on {HOST}:{PORT}")

conn,addr = ss.accept() # waits for client 
with conn:  #will automatically close the connection
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    if data:
        print(f"Received from client: {data.decode('utf-8')}")
    else:
        print("No data recieved from client")
    