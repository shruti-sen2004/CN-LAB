import socket 
import threading

def handle_client(c,a):
    print(f"\nConnected to {a}")
    while True:
        try:
            msg = c.recv(1024).decode()
            if not msg:
                break
            print(f"{a}:{msg}")
        except Exception:
            break
    c.close()
    print(f"\nClient {a} disconnected")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",12345))
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.listen(2) 

while True:
    c,a = s.accept()
    threading.Thread(target=handle_client, args=(c,a,)).start()

