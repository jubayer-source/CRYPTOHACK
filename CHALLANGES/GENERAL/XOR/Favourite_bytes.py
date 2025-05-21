def xor_with_single_byte(data, key):
    return bytes([b^key for b in data])

ciphertext = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

# Try every possible single-byte key
for key in range(256):
    plaintext = xor_with_single_byte(ciphertext, key)
    try:
        decoded = plaintext.decode()
        if decoded.isprintable():
            print(f"key: {key} - {decoded}")
    except UnicodeDecodeError:
        continue
