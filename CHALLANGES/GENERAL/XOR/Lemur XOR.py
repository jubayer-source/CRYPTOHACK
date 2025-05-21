from PIL import Image
import numpy as np

# Load both images after downloading 
lemur = Image.open("/home/jubayer/Downloads/lemur.png").convert("RGB")
flag = Image.open("/home/jubayer/Downloads/flag.png").convert("RGB")

# Convert to NumPy arrays
lemur_data = np.array(lemur)
flag_data = np.array(flag)

# XOR pixel-by-pixel
xor_result = np.bitwise_xor(lemur_data, flag_data)

# Convert back to image
result_image = Image.fromarray(xor_result)

# Save the XOR result
result_image.save("xor_output.png")
result_image.show()  # Optional: to visually inspect
