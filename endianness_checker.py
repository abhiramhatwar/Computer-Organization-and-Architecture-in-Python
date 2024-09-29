import struct

def check_endianness():
    return 'Little Endian' if struct.pack('H', 1) == b'\x01\x00' else 'Big Endian'

def visualize_endianness(value):
    packed_little = struct.pack('<I', value)
    packed_big = struct.pack('>I', value)
    
    little_endian_representation = " ".join(f"{byte:02x}" for byte in packed_little)
    big_endian_representation = " ".join(f"{byte:02x}" for byte in packed_big)
    
    print(f"\nMemory Representation for value {value}:")
    print(f"Little Endian: {little_endian_representation}")
    print(f"Big Endian:    {big_endian_representation}")

def main():
    system_endianness = check_endianness()
    print(f"System Endianness: {system_endianness}")
    
    try:
        value = int(input("Enter an integer value (0-4294967295): "))
        if value < 0 or value > 4294967295:
            print("Please enter a value between 0 and 4294967295.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    visualize_endianness(value)

if __name__ == "__main__":
    main()
