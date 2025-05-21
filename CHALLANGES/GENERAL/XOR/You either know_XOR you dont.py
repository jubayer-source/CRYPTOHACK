def xor_with_single_byte(data, key):
    return bytes([b ^ key for b in data])

# Encrypted flag in hex
ciphertext = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print("Ciphertext in bytes:", ciphertext)

# Try all possible single-byte keys (0–255)
for key in range(256):
    plaintext = xor_with_single_byte(ciphertext, key)
    
    try:
        decoded = plaintext.decode()
        # Debugging: print the first 20 characters of the decoded text
        print(f"Key: {key} → {decoded[:20]}...")  # Print a snippet of the decoded text
        
        # Check if it starts with the flag format (e.g., 'flag{')
        if decoded.startswith("flag{"):
            print(f"Key: {key} → {decoded}")
            break  # Stop after finding the correct key
    except UnicodeDecodeError:
        # Handle non-UTF-8 characters
        print(f"Key: {key} → Invalid UTF-8 sequence")
        continue



# ANOTHER SOLUTION IS Bellow: 


from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode()))
# This gives us the key
print(xor(flag, 'myXORkey'.encode()))
# using the output of key, and gussing the 'y' we get the key.

# encoding to bytes using `.encode`, it only changes `data type`, not the data

# Credit: oushanmu