hex_data = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

# convert hex to bytes
decoded_bytes = bytes.fromhex(hex_data)

# convert bytes to ASCII string
flag = decoded_bytes.decode('utf-8')

print("The Flag is:", flag)