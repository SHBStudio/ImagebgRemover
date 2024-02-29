from rembg import remove
from PIL import Image

input_path = 'assets\image.jpg'
output_path = 'assets\output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)