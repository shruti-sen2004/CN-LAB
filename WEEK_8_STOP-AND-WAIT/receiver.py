import socket
import random

# Set up receiver socket
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.bind(('localhost', 12345))

expected_seq = 0

while True:
    data, addr = receiver_socket.recvfrom(1024) # used for UDP
    message = data.decode()
    
    if ':' in message:
        seq_num, packet = message.split(':', 1)
        seq_num = int(seq_num)
        print(f"\nReceived: {packet} with Seq #{seq_num}")

        # Simulate packet drop with 30% probability
        if random.random() < 0.3:
            print("Simulating packet loss... No ACK sent.")
            continue

        if seq_num == expected_seq:
            print("Packet OK. Sending ACK...")
            ack = f"ACK{seq_num}"
            receiver_socket.sendto(ack.encode(), addr)
            expected_seq = 1 - expected_seq
        else:
            print("Duplicate packet. Resending last ACK...")
            ack = f"ACK{1 - expected_seq}"
            receiver_socket.sendto(ack.encode(), addr)