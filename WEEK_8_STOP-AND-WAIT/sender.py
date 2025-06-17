import socket
import time

# Set up sender socket
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_address = ('localhost', 12345)

sender_socket.settimeout(2) # time out of 2 sec

data_packets = ['Packet1', 'Packet2', 'Packet3']
seq_num = 0

for packet in data_packets:
    ack_received = False
    while not ack_received:
        message = f"{seq_num}:{packet}"
        sender_socket.sendto(message.encode(), receiver_address)
        print(f"Sent: {message}")
        try:
            # _ is used for variables that will store values that
            # are never used
            ack, _ = sender_socket.recvfrom(1024)
            ack = ack.decode()
            if ack == f"ACK{seq_num}":
                print(f"Received: {ack}")
                ack_received = True
                seq_num = 1 - seq_num  # Alternate between 0 and 1
            else:
                print("Incorrect ACK received, resending...")
        except socket.timeout:
            print("ACK not received. Resending...")

sender_socket.close()