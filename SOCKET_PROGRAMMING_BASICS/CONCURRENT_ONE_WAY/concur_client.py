import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",12345))

while True:
    msg = input("Enter your message: ")
    if msg.lower() == "exit":
        break
    s.sendall(msg.encode("utf-8"))
s.close()
    
