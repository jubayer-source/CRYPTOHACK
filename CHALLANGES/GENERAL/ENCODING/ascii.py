ascii_valuess = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

#convert each number to its ASCII character
flag = ''.join(chr(n) for n in ascii_valuess)

print("Flag is:", flag)


