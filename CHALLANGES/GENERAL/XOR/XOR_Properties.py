from binascii import unhexlify

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Given hex values
KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY1_KEY2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
Encrypted_flag = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# Recover KEY2
KEY2 = xor_bytes(KEY1, KEY1_KEY2)

# Recover KEY3
KEY3 = xor_bytes(KEY2, KEY2_KEY3)

# combined_key = KEY1 ^ KEY2 ^ KEY3
combined_key = xor_bytes(KEY1, xor_bytes(KEY2, KEY3))

# Decrypt flag
Flag = xor_bytes(Encrypted_flag, combined_key)

# Print flag as string (ignore decoding errors or use latin-1)
try:
    print("Flag is:", Flag.decode('utf-8'))
except UnicodeDecodeError:
    print("Flag is (latin1 decoded):", Flag.decode('latin-1'))
    # You can also just print raw bytes:
    # print("Flag is:", Flag)
