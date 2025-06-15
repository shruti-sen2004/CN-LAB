def generate_hamming_code(data_bits):
    """Generates a Hamming (7,4) code for 4-bit data."""
    p1 = data_bits[0] ^ data_bits[1] ^ data_bits[3]
    p2 = data_bits[0] ^ data_bits[2] ^ data_bits[3]
    p3 = data_bits[1] ^ data_bits[2] ^ data_bits[3]
    
    return [p1, p2, data_bits[0], p3, data_bits[1], data_bits[2], data_bits[3]]

def detect_errors(sent_code, received_code):
    """Detects 1-bit and 2-bit errors in a received Hamming (7,4) code."""
    p1 = received_code[0] ^ received_code[2] ^ received_code[4] ^ received_code[6]
    p2 = received_code[1] ^ received_code[2] ^ received_code[5] ^ received_code[6]
    p3 = received_code[3] ^ received_code[4] ^ received_code[5] ^ received_code[6]
    
    error_position = p1 + (p2 << 1) + (p3 << 2)
    
    if received_code == sent_code:
        return "No error detected."
    elif 1 <= error_position <= 7:
        return f"Single-bit error detected at position {error_position}."
    else:
        return "Two-bit error detected or uncorrectable error."

# Taking user input for sent and received data
sent_data = list(map(int, input("Enter 4-bit sent data (space-separated): ").split()))
received_data = list(map(int, input("Enter 7-bit received data (space-separated): ").split()))

# Generate Hamming code for sent data
sent_hamming_code = generate_hamming_code(sent_data)
print("Generated Hamming Code for Sent Data:", sent_hamming_code)

# Detect errors
print("Received Code:", received_data)
print(detect_errors(sent_hamming_code, received_data))
