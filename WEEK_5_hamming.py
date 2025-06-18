def generate_hamming_code(d): # Generates a Hamming (7,4) code for 4-bit data.
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    
    return f"{p1}{p2}{d[0]}{p3}{d[1]}{d[2]}{d[3]}"

def detect_errors(sc, rc):   #Detects 1-bit and 2-bit errors in a received Hamming (7,4) code.
    p1 = rc[0] ^ rc[2] ^ rc[4] ^ rc[6]
    p2 = rc[1] ^ rc[2] ^ rc[5] ^ rc[6]
    p3 = rc[3] ^ rc[4] ^ rc[5] ^ rc[6]
    
    err_pos = p1 + (p2 * 2) + (p3 * 4)
    
    if rc == sc:
        return "No error detected."
    elif 1 <= err_pos <= 7:
        rc[err_pos-1] = 1 - rc[err_pos-1]
        if rc == sc :
            new_rc = int(''.join(map(str, rc)))
            return f"Single-bit error detected at position {err_pos}\nCorrected received code is {new_rc}"
        else:
            return "Two-bit error detected or uncorrectable error."
    else:
        return "Two-bit error detected or uncorrectable error."

# Taking user input for sent and received data
sent_data = [int(bit) for bit in input("Enter 4-bit sent data: ")]
# Generate Hamming code for sent data
sent_hamming_code = generate_hamming_code(sent_data)
print("Generated Hamming Code for Sent Data:", sent_hamming_code)

# Detect errors
received_data = [int(bit) for bit in input("\nEnter 7-bit received data: ")]
print(detect_errors(sent_hamming_code, received_data))
