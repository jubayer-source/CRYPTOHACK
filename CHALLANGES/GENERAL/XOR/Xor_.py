orginal = "label"
xor_key = 13

new_string = ''.join([chr(ord(c)^ xor_key) for c in orginal])

flag = f"crypto{{{new_string}}}"

print(flag)

# Another way to solve:

given = "label"

print("crypto{", end="")
for x in given:
  print(chr(ord(x)^13), end="")
print("}")
