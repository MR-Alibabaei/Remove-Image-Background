from rembg import remove
from PIL import Image

input_path = "test/2.jpg"
output_path = "test/2_out.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
