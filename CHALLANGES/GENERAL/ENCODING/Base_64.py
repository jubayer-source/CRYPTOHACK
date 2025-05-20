import base64

## Guideline: Take the below hex string, decode it into bytes and then encode it into Base64.
# Step 1: Given hex string
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 2: Convert hex string to bytes
decoded_bytes = bytes.fromhex(hex_string)

# Step 3: Encode the bytes into Base64
base64_encoded = base64.b64encode(decoded_bytes)

# Step 4: Convert the Base64 bytes to string and print it
print("Base64 Encoded Flag is:", base64_encoded.decode('utf-8'))
