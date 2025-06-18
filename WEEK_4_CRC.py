
def compute_crc(data: str, divisor: str) -> str:   # Computes the CRC remainder 
    # Convert input strings to lists for easier manipulation
    data_bits = list(data)
    divisor_bits = list(divisor)
    n= len(divisor_bits)

    # Number of zeros to append to data_bits is one less than the length of divisor_bits
    data_bits_extended = data_bits + ["0"] * (n- 1)

    # Perform the long division
    for i in range(len(data_bits)):
        # If the current bit is 1, then XOR with divisor
        if data_bits_extended[i] == "1":
            for j in range(n):
                # XOR each bit
                data_bits_extended[i + j] = str(
                    int(data_bits_extended[i + j]) ^ int(divisor_bits[j])
                )

    # Extract the remainder bits from data_bits_extendend 
    remainder = "".join(data_bits_extended[-(n-1) :])
    return remainder


def generate_transmitted_frame(data: str, divisor: str) -> str:  # Generates the transmitted frame
    remainder = compute_crc(data, divisor)
    return data + remainder


def verify_crc(received_data: str, divisor: str) -> bool:   #  Verifies if the received data (with CRC) has any error
    remainder = compute_crc(received_data, divisor) 
    return all(bit == "0" for bit in remainder)    # If remainder is all zeros, then no error generates true


if __name__ == "__main__":
    print(f"--- SENDER SIDE ---")
    data = input("Enter the binary data (e.g. 1101011011): ").strip()
    divisor = input("Enter the binary divisor (e.g. 10011): ").strip()

    # Generate transmitted frame
    transmitted_frame = generate_transmitted_frame(data, divisor)
    print(f"Transmitted Frame (Data + CRC): {transmitted_frame}")

    # Simulate receiving the transmitted frame
    print(f"\n--- RECEIVER SIDE ---")
    received_frame = input("Enter the received frame for verification (leave blank to use the transmitted frame): "
    ).strip()
    if not received_frame:
        received_frame = transmitted_frame

    # Verify the received frame
    if verify_crc(received_frame, divisor):
        print("CRC check passed. No error detected.")
    else:
        print("CRC check failed. Error detected.")

