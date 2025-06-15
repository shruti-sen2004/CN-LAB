import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 2566

server_socket.bind((host, port))
server_socket.listen(2)
print("Server is listening on port: ", port)

client_socket, client_address = server_socket.accept()
print("Connection from: ", client_address)

while True:
    data = client_socket.recv(1024).decode()
    if data.lower() == 'exit':
        print("Client has exited the connection.")
        break
    print("Recieved from client: ", data)
    client_socket.send(data.encode())

client_socket.close()
server_socket.close()