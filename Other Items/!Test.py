import os
from PIL import Image
import numpy as np

# Define the output folder
output_folder = "Portraits"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the region coordinates
x1, y1 = 130, 270
x2, y2 = 989, 919

# Get a list of PNG files in the current directory
png_files = [file for file in os.listdir() if file.endswith(".png")]
jpg_files = [file for file in os.listdir() if file.endswith(".jpg")]

# Process each PNG file
for png_file in png_files:
    # Open the image
    image = Image.open(png_file).convert("RGBA")

    # Crop the image to the specified region
    scaled_image = image.resize((85, 64), Image.NEAREST)

    # Testing
    img = scaled_image
    width = img.size[0] 
    height = img.size[1] 
    for i in range(0,width):# process all pixels
        for j in range(0,height):
            data = img.getpixel((i,j))
            # data[0] = Red,  [1] = Green, [2] = Blue
            # data[0,1,2] range = 0~255
            # Beast Palletes
            if data[0] == 238 and data[1] == 167 and data[2] == 109:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 229 and data[1] == 158 and data[2] == 105:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 220 and data[1] == 148 and data[2] == 101:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 238 and data[1] == 130 and data[2] == 114:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 242 and data[1] == 151 and data[2] == 99:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 246 and data[1] == 169 and data[2] == 92:
                img.putpixel((i,j),(0, 0, 0, 0))
            # Undead Palletes
            if data[0] == 194 and data[1] == 194 and data[2] == 173:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 173 and data[1] == 186 and data[2] == 160:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 151 and data[1] == 182 and data[2] == 158:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 203 and data[1] == 195 and data[2] == 135:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 169 and data[1] == 194 and data[2] == 135:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 127 and data[1] == 190 and data[2] == 140:
                img.putpixel((i,j),(0, 0, 0, 0))
            # Tech Palletes
            if data[0] == 150 and data[1] == 225 and data[2] == 216:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 149 and data[1] == 206 and data[2] == 233:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 157 and data[1] == 183 and data[2] == 246:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 178 and data[1] == 219 and data[2] == 220:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 162 and data[1] == 209 and data[2] == 225:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 168 and data[1] == 192 and data[2] == 216:
                img.putpixel((i,j),(0, 0, 0, 0))
            # MAGICK Palletes
            if data[0] == 220 and data[1] == 178 and data[2] == 210:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 225 and data[1] == 162 and data[2] == 197:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 220 and data[1] == 147 and data[2] == 179:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 232 and data[1] == 167 and data[2] == 238:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 242 and data[1] == 143 and data[2] == 208:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 255 and data[1] == 123 and data[2] == 165:
                img.putpixel((i,j),(0, 0, 0, 0))
            # Terrain Palletes
            if data[0] == 212 and data[1] == 201 and data[2] == 171:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 203 and data[1] == 189 and data[2] == 169:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 190 and data[1] == 182 and data[2] == 169:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 242 and data[1] == 213 and data[2] == 131:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 238 and data[1] == 189 and data[2] == 116:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 216 and data[1] == 169 and data[2] == 134:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 246 and data[1] == 233 and data[2] == 160:
                img.putpixel((i,j),(0, 0, 0, 0))
            
            data720 = img.getpixel((72,0)) # Temples
            img.putpixel((45,0),(0, 0, 0, 0))
            img.putpixel((46,0),(0, 0, 0, 0))
            img.putpixel((47,0),(0, 0, 0, 0))
            img.putpixel((48,0),(0, 0, 0, 0))
            img.putpixel((49,0),(0, 0, 0, 0))
            img.putpixel((50,0),(0, 0, 0, 0))
            img.putpixel((51,0),(0, 0, 0, 0))
            img.putpixel((52,0),(0, 0, 0, 0))
            img.putpixel((53,0),(0, 0, 0, 0))
            img.putpixel((54,0),(0, 0, 0, 0))
            # Attack Pixels 
            if data720[0] == 207 and data720[1] == 122 and data720[2] == 76:
                img.putpixel((6,57),(0, 0, 0, 0))
                img.putpixel((11,57),(0, 0, 0, 0))
                img.putpixel((6,58),(0, 0, 0, 0))
                img.putpixel((5,58),(0, 0, 0, 0))
                img.putpixel((11,58),(0, 0, 0, 0))
                img.putpixel((12,58),(0, 0, 0, 0))
                img.putpixel((6,59),(0, 0, 0, 0))
                img.putpixel((5,59),(0, 0, 0, 0))
                img.putpixel((11,59),(0, 0, 0, 0))
                img.putpixel((12,59),(0, 0, 0, 0))
                img.putpixel((2,60),(0, 0, 0, 0))
                img.putpixel((15,60),(0, 0, 0, 0))
                img.putpixel((1,61),(0, 0, 0, 0))
                img.putpixel((2,61),(0, 0, 0, 0))
                img.putpixel((5,61),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((11,61),(0, 0, 0, 0))
                img.putpixel((12,61),(0, 0, 0, 0))
                img.putpixel((15,61),(0, 0, 0, 0))
                img.putpixel((16,61),(0, 0, 0, 0))
                img.putpixel((1,62),(0, 0, 0, 0))
                img.putpixel((2,62),(0, 0, 0, 0))
                img.putpixel((4,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((6,62),(0, 0, 0, 0))
                img.putpixel((7,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((11,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((13,62),(0, 0, 0, 0))
                img.putpixel((15,62),(0, 0, 0, 0))
                img.putpixel((16,62),(0, 0, 0, 0))
                img.putpixel((4,63),(0, 0, 0, 0))
                img.putpixel((5,63),(0, 0, 0, 0))
                img.putpixel((6,63),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((8,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
                img.putpixel((10,63),(0, 0, 0, 0))
                img.putpixel((11,63),(0, 0, 0, 0))
                img.putpixel((12,63),(0, 0, 0, 0))
                img.putpixel((13,63),(0, 0, 0, 0))
            elif data720[0] == 203 and data720[1] == 128 and data720[2] == 178:
                img.putpixel((8,56),(0, 0, 0, 0))
                img.putpixel((8,57),(0, 0, 0, 0))
                img.putpixel((8,58),(0, 0, 0, 0))
                img.putpixel((10,58),(0, 0, 0, 0))
                img.putpixel((4,59),(0, 0, 0, 0))
                img.putpixel((10,59),(0, 0, 0, 0))
                img.putpixel((8,60),(0, 0, 0, 0))
                img.putpixel((9,60),(0, 0, 0, 0))
                img.putpixel((13,60),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((7,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((12,61),(0, 0, 0, 0))
                img.putpixel((14,61),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((6,62),(0, 0, 0, 0))
                img.putpixel((7,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((13,62),(0, 0, 0, 0))
                img.putpixel((5,63),(0, 0, 0, 0))
                img.putpixel((6,63),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((8,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
            elif data720[0] == 199 and data720[1] == 175 and data720[2] == 160:
                img.putpixel((8,57),(0, 0, 0, 0))
                img.putpixel((7,58),(0, 0, 0, 0))
                img.putpixel((8,58),(0, 0, 0, 0))
                img.putpixel((9,58),(0, 0, 0, 0))
                img.putpixel((7,59),(0, 0, 0, 0))
                img.putpixel((8,59),(0, 0, 0, 0))
                img.putpixel((9,59),(0, 0, 0, 0))
                img.putpixel((5,61),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((7,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((10,61),(0, 0, 0, 0))
                img.putpixel((11,61),(0, 0, 0, 0))
                img.putpixel((4,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((6,62),(0, 0, 0, 0))
                img.putpixel((7,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((11,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
                img.putpixel((10,63),(0, 0, 0, 0))
            elif data720[0] == 220 and data720[1] == 147 and data720[2] == 101:
                img.putpixel((8,57),(0, 0, 0, 0))
                img.putpixel((7,58),(0, 0, 0, 0))
                img.putpixel((8,58),(0, 0, 0, 0))
                img.putpixel((9,58),(0, 0, 0, 0))
                img.putpixel((7,59),(0, 0, 0, 0))
                img.putpixel((8,59),(0, 0, 0, 0))
                img.putpixel((9,59),(0, 0, 0, 0))
                img.putpixel((5,61),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((7,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((10,61),(0, 0, 0, 0))
                img.putpixel((11,61),(0, 0, 0, 0))
                img.putpixel((4,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((6,62),(0, 0, 0, 0))
                img.putpixel((7,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((11,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
                img.putpixel((10,63),(0, 0, 0, 0))
            elif data720[0] == 182 and data720[1] == 152 and data720[2] == 116:
                img.putpixel((9,54),(0, 0, 0, 0))
                img.putpixel((9,55),(0, 0, 0, 0))
                img.putpixel((12,55),(0, 0, 0, 0))
                img.putpixel((8,56),(0, 0, 0, 0))
                img.putpixel((9,56),(0, 0, 0, 0))
                img.putpixel((12,56),(0, 0, 0, 0))
                img.putpixel((5,57),(0, 0, 0, 0))
                img.putpixel((8,57),(0, 0, 0, 0))
                img.putpixel((9,57),(0, 0, 0, 0))
                img.putpixel((11,57),(0, 0, 0, 0))
                img.putpixel((12,57),(0, 0, 0, 0))
                img.putpixel((5,58),(0, 0, 0, 0))
                img.putpixel((11,58),(0, 0, 0, 0))
                img.putpixel((12,58),(0, 0, 0, 0))
                img.putpixel((2,59),(0, 0, 0, 0))
                img.putpixel((5,59),(0, 0, 0, 0))
                img.putpixel((6,59),(0, 0, 0, 0))
                img.putpixel((8,59),(0, 0, 0, 0))
                img.putpixel((2,60),(0, 0, 0, 0))
                img.putpixel((5,60),(0, 0, 0, 0))
                img.putpixel((6,60),(0, 0, 0, 0))
                img.putpixel((8,60),(0, 0, 0, 0))
                img.putpixel((12,60),(0, 0, 0, 0))
                img.putpixel((2,61),(0, 0, 0, 0))
                img.putpixel((3,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((12,61),(0, 0, 0, 0))
                img.putpixel((2,62),(0, 0, 0, 0))
                img.putpixel((3,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((16,62),(0, 0, 0, 0))
                img.putpixel((2,63),(0, 0, 0, 0))
                img.putpixel((3,63),(0, 0, 0, 0))
                img.putpixel((5,63),(0, 0, 0, 0))
                img.putpixel((6,63),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((8,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
                img.putpixel((12,63),(0, 0, 0, 0))
                img.putpixel((15,63),(0, 0, 0, 0))
                img.putpixel((16,63),(0, 0, 0, 0))
            elif data720[0] == 183 and data720[1] == 152 and data720[2] == 203:
                img.putpixel((9,56),(0, 0, 0, 0))
                img.putpixel((9,57),(0, 0, 0, 0))
                img.putpixel((8,58),(0, 0, 0, 0))
                img.putpixel((9,58),(0, 0, 0, 0))
                img.putpixel((8,59),(0, 0, 0, 0))
                img.putpixel((9,59),(0, 0, 0, 0))
                img.putpixel((10,59),(0, 0, 0, 0))
                img.putpixel((5,60),(0, 0, 0, 0))
                img.putpixel((6,60),(0, 0, 0, 0))
                img.putpixel((8,60),(0, 0, 0, 0))
                img.putpixel((9,60),(0, 0, 0, 0))
                img.putpixel((10,60),(0, 0, 0, 0))
                img.putpixel((11,60),(0, 0, 0, 0))
                img.putpixel((12,60),(0, 0, 0, 0))
                img.putpixel((4,61),(0, 0, 0, 0))
                img.putpixel((5,61),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((11,61),(0, 0, 0, 0))
                img.putpixel((12,61),(0, 0, 0, 0))
                img.putpixel((13,61),(0, 0, 0, 0))
                img.putpixel((4,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((13,62),(0, 0, 0, 0))
                img.putpixel((3,63),(0, 0, 0, 0))
                img.putpixel((4,63),(0, 0, 0, 0))
                img.putpixel((8,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
            # Health
            img.putpixel((71,0),(0, 0, 0, 0))
            img.putpixel((72,0),(0, 0, 0, 0))
            img.putpixel((73,0),(0, 0, 0, 0))
            img.putpixel((74,0),(0, 0, 0, 0))
            img.putpixel((75,0),(0, 0, 0, 0))
            img.putpixel((76,0),(0, 0, 0, 0))
            img.putpixel((77,0),(0, 0, 0, 0))
            img.putpixel((78,0),(0, 0, 0, 0))
            img.putpixel((79,0),(0, 0, 0, 0))
            img.putpixel((80,0),(0, 0, 0, 0))
            img.putpixel((81,0),(0, 0, 0, 0))
            img.putpixel((82,0),(0, 0, 0, 0))
            img.putpixel((83,0),(0, 0, 0, 0))
            img.putpixel((72,1),(0, 0, 0, 0))
            img.putpixel((73,1),(0, 0, 0, 0))
            img.putpixel((74,1),(0, 0, 0, 0))
            img.putpixel((75,1),(0, 0, 0, 0))
            img.putpixel((76,1),(0, 0, 0, 0))
            img.putpixel((77,1),(0, 0, 0, 0))
            img.putpixel((78,1),(0, 0, 0, 0))
            img.putpixel((79,1),(0, 0, 0, 0))
            img.putpixel((80,1),(0, 0, 0, 0))
            img.putpixel((81,1),(0, 0, 0, 0))
            img.putpixel((82,1),(0, 0, 0, 0))
            img.putpixel((74,2),(0, 0, 0, 0))
            img.putpixel((75,2),(0, 0, 0, 0))
            img.putpixel((76,2),(0, 0, 0, 0))
            img.putpixel((77,2),(0, 0, 0, 0))
            img.putpixel((78,2),(0, 0, 0, 0))
            img.putpixel((79,2),(0, 0, 0, 0))
            img.putpixel((80,2),(0, 0, 0, 0))
            img.putpixel((75,3),(0, 0, 0, 0))
            img.putpixel((76,3),(0, 0, 0, 0))
            img.putpixel((77,3),(0, 0, 0, 0))
            img.putpixel((78,3),(0, 0, 0, 0))
            img.putpixel((79,3),(0, 0, 0, 0))
            img.putpixel((76,4),(0, 0, 0, 0))
            img.putpixel((77,4),(0, 0, 0, 0))
            img.putpixel((78,4),(0, 0, 0, 0))
            img.putpixel((77,5),(0, 0, 0, 0))

    # Save the cropped image in the "Portraits" folder with the same filename
    output_path = os.path.join(output_folder, png_file)
    img.save(output_path)

    print(f"Cropped image saved: {output_path}")

# Process each JPG file
for jpg_file in jpg_files:
    # Open the image
    image = Image.open(jpg_file).convert("RGBA")

    # Crop the image to the specified region
    scaled_image = image.resize((85, 64), Image.NEAREST)

    # Testing
    img = scaled_image
    width = img.size[0] 
    height = img.size[1] 
    for i in range(0,width):# process all pixels
        for j in range(0,height):
            data = img.getpixel((i,j))
            # data[0] = Red,  [1] = Green, [2] = Blue
            # data[0,1,2] range = 0~255
            # Beast Palletes
            if data[0] == 238 and data[1] == 167 and data[2] == 109:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 229 and data[1] == 158 and data[2] == 105:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 220 and data[1] == 148 and data[2] == 101:
                img.putpixel((i,j),(0, 0, 0, 0))
            
            if data[0] == 238 and data[1] == 130 and data[2] == 114:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 242 and data[1] == 151 and data[2] == 99:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 246 and data[1] == 169 and data[2] == 92:
                img.putpixel((i,j),(0, 0, 0, 0))
            # Undead Palletes
            if data[0] == 194 and data[1] == 194 and data[2] == 173:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 173 and data[1] == 186 and data[2] == 160:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 151 and data[1] == 182 and data[2] == 158:
                img.putpixel((i,j),(0, 0, 0, 0))
            
            if data[0] == 203 and data[1] == 195 and data[2] == 135:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 169 and data[1] == 194 and data[2] == 135:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 127 and data[1] == 190 and data[2] == 140:
                img.putpixel((i,j),(0, 0, 0, 0))
            # Tech Palletes
            if data[0] == 150 and data[1] == 225 and data[2] == 216:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 149 and data[1] == 206 and data[2] == 233:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 157 and data[1] == 183 and data[2] == 246:
                img.putpixel((i,j),(0, 0, 0, 0))
            
            if data[0] == 178 and data[1] == 219 and data[2] == 220:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 162 and data[1] == 209 and data[2] == 225:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 168 and data[1] == 192 and data[2] == 216:
                img.putpixel((i,j),(0, 0, 0, 0))
            # MAGICK Palletes
            if data[0] == 220 and data[1] == 178 and data[2] == 210:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 225 and data[1] == 162 and data[2] == 197:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 220 and data[1] == 147 and data[2] == 179:
                img.putpixel((i,j),(0, 0, 0, 0))
            
            if data[0] == 232 and data[1] == 167 and data[2] == 238:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 242 and data[1] == 143 and data[2] == 208:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 255 and data[1] == 123 and data[2] == 165:
                img.putpixel((i,j),(0, 0, 0, 0))
            # Terrain Palletes
            if data[0] == 212 and data[1] == 201 and data[2] == 171:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 203 and data[1] == 189 and data[2] == 169:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 190 and data[1] == 182 and data[2] == 169:
                img.putpixel((i,j),(0, 0, 0, 0))
            
            if data[0] == 242 and data[1] == 213 and data[2] == 131:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 238 and data[1] == 189 and data[2] == 116:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 216 and data[1] == 169 and data[2] == 134:
                img.putpixel((i,j),(0, 0, 0, 0))
            if data[0] == 246 and data[1] == 233 and data[2] == 160:
                img.putpixel((i,j),(0, 0, 0, 0))
            
            data720 = img.getpixel((72,0)) # Temples
            img.putpixel((45,0),(0, 0, 0, 0))
            img.putpixel((46,0),(0, 0, 0, 0))
            img.putpixel((47,0),(0, 0, 0, 0))
            img.putpixel((48,0),(0, 0, 0, 0))
            img.putpixel((49,0),(0, 0, 0, 0))
            img.putpixel((50,0),(0, 0, 0, 0))
            img.putpixel((51,0),(0, 0, 0, 0))
            img.putpixel((52,0),(0, 0, 0, 0))
            img.putpixel((53,0),(0, 0, 0, 0))
            img.putpixel((54,0),(0, 0, 0, 0))
            # Attack Pixels 
            if data720[0] == 207 and data720[1] == 122 and data720[2] == 76:
                img.putpixel((6,57),(0, 0, 0, 0))
                img.putpixel((11,57),(0, 0, 0, 0))
                img.putpixel((6,58),(0, 0, 0, 0))
                img.putpixel((5,58),(0, 0, 0, 0))
                img.putpixel((11,58),(0, 0, 0, 0))
                img.putpixel((12,58),(0, 0, 0, 0))
                img.putpixel((6,59),(0, 0, 0, 0))
                img.putpixel((5,59),(0, 0, 0, 0))
                img.putpixel((11,59),(0, 0, 0, 0))
                img.putpixel((12,59),(0, 0, 0, 0))
                img.putpixel((2,60),(0, 0, 0, 0))
                img.putpixel((15,60),(0, 0, 0, 0))
                img.putpixel((1,61),(0, 0, 0, 0))
                img.putpixel((2,61),(0, 0, 0, 0))
                img.putpixel((5,61),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((11,61),(0, 0, 0, 0))
                img.putpixel((12,61),(0, 0, 0, 0))
                img.putpixel((15,61),(0, 0, 0, 0))
                img.putpixel((16,61),(0, 0, 0, 0))
                img.putpixel((1,62),(0, 0, 0, 0))
                img.putpixel((2,62),(0, 0, 0, 0))
                img.putpixel((4,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((6,62),(0, 0, 0, 0))
                img.putpixel((7,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((11,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((13,62),(0, 0, 0, 0))
                img.putpixel((15,62),(0, 0, 0, 0))
                img.putpixel((16,62),(0, 0, 0, 0))
                img.putpixel((4,63),(0, 0, 0, 0))
                img.putpixel((5,63),(0, 0, 0, 0))
                img.putpixel((6,63),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((8,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
                img.putpixel((10,63),(0, 0, 0, 0))
                img.putpixel((11,63),(0, 0, 0, 0))
                img.putpixel((12,63),(0, 0, 0, 0))
                img.putpixel((13,63),(0, 0, 0, 0))
            elif data720[0] == 203 and data720[1] == 128 and data720[2] == 178:
                img.putpixel((8,56),(0, 0, 0, 0))
                img.putpixel((8,57),(0, 0, 0, 0))
                img.putpixel((8,58),(0, 0, 0, 0))
                img.putpixel((10,58),(0, 0, 0, 0))
                img.putpixel((4,59),(0, 0, 0, 0))
                img.putpixel((10,59),(0, 0, 0, 0))
                img.putpixel((8,60),(0, 0, 0, 0))
                img.putpixel((9,60),(0, 0, 0, 0))
                img.putpixel((13,60),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((7,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((12,61),(0, 0, 0, 0))
                img.putpixel((14,61),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((6,62),(0, 0, 0, 0))
                img.putpixel((7,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((13,62),(0, 0, 0, 0))
                img.putpixel((5,63),(0, 0, 0, 0))
                img.putpixel((6,63),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((8,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
            elif data720[0] == 199 and data720[1] == 175 and data720[2] == 160:
                img.putpixel((8,57),(0, 0, 0, 0))
                img.putpixel((7,58),(0, 0, 0, 0))
                img.putpixel((8,58),(0, 0, 0, 0))
                img.putpixel((9,58),(0, 0, 0, 0))
                img.putpixel((7,59),(0, 0, 0, 0))
                img.putpixel((8,59),(0, 0, 0, 0))
                img.putpixel((9,59),(0, 0, 0, 0))
                img.putpixel((5,61),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((7,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((10,61),(0, 0, 0, 0))
                img.putpixel((11,61),(0, 0, 0, 0))
                img.putpixel((4,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((6,62),(0, 0, 0, 0))
                img.putpixel((7,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((11,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
                img.putpixel((10,63),(0, 0, 0, 0))
            elif data720[0] == 220 and data720[1] == 147 and data720[2] == 101:
                img.putpixel((8,57),(0, 0, 0, 0))
                img.putpixel((7,58),(0, 0, 0, 0))
                img.putpixel((8,58),(0, 0, 0, 0))
                img.putpixel((9,58),(0, 0, 0, 0))
                img.putpixel((7,59),(0, 0, 0, 0))
                img.putpixel((8,59),(0, 0, 0, 0))
                img.putpixel((9,59),(0, 0, 0, 0))
                img.putpixel((5,61),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((7,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((10,61),(0, 0, 0, 0))
                img.putpixel((11,61),(0, 0, 0, 0))
                img.putpixel((4,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((6,62),(0, 0, 0, 0))
                img.putpixel((7,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((11,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
                img.putpixel((10,63),(0, 0, 0, 0))
            elif data720[0] == 182 and data720[1] == 152 and data720[2] == 116:
                img.putpixel((9,54),(0, 0, 0, 0))
                img.putpixel((9,55),(0, 0, 0, 0))
                img.putpixel((12,55),(0, 0, 0, 0))
                img.putpixel((8,56),(0, 0, 0, 0))
                img.putpixel((9,56),(0, 0, 0, 0))
                img.putpixel((12,56),(0, 0, 0, 0))
                img.putpixel((5,57),(0, 0, 0, 0))
                img.putpixel((8,57),(0, 0, 0, 0))
                img.putpixel((9,57),(0, 0, 0, 0))
                img.putpixel((11,57),(0, 0, 0, 0))
                img.putpixel((12,57),(0, 0, 0, 0))
                img.putpixel((5,58),(0, 0, 0, 0))
                img.putpixel((11,58),(0, 0, 0, 0))
                img.putpixel((12,58),(0, 0, 0, 0))
                img.putpixel((2,59),(0, 0, 0, 0))
                img.putpixel((5,59),(0, 0, 0, 0))
                img.putpixel((6,59),(0, 0, 0, 0))
                img.putpixel((8,59),(0, 0, 0, 0))
                img.putpixel((2,60),(0, 0, 0, 0))
                img.putpixel((5,60),(0, 0, 0, 0))
                img.putpixel((6,60),(0, 0, 0, 0))
                img.putpixel((8,60),(0, 0, 0, 0))
                img.putpixel((12,60),(0, 0, 0, 0))
                img.putpixel((2,61),(0, 0, 0, 0))
                img.putpixel((3,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((12,61),(0, 0, 0, 0))
                img.putpixel((2,62),(0, 0, 0, 0))
                img.putpixel((3,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((16,62),(0, 0, 0, 0))
                img.putpixel((2,63),(0, 0, 0, 0))
                img.putpixel((3,63),(0, 0, 0, 0))
                img.putpixel((5,63),(0, 0, 0, 0))
                img.putpixel((6,63),(0, 0, 0, 0))
                img.putpixel((7,63),(0, 0, 0, 0))
                img.putpixel((8,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
                img.putpixel((12,63),(0, 0, 0, 0))
                img.putpixel((15,63),(0, 0, 0, 0))
                img.putpixel((16,63),(0, 0, 0, 0))
            elif data720[0] == 183 and data720[1] == 152 and data720[2] == 203:
                img.putpixel((9,56),(0, 0, 0, 0))
                img.putpixel((9,57),(0, 0, 0, 0))
                img.putpixel((8,58),(0, 0, 0, 0))
                img.putpixel((9,58),(0, 0, 0, 0))
                img.putpixel((8,59),(0, 0, 0, 0))
                img.putpixel((9,59),(0, 0, 0, 0))
                img.putpixel((10,59),(0, 0, 0, 0))
                img.putpixel((5,60),(0, 0, 0, 0))
                img.putpixel((6,60),(0, 0, 0, 0))
                img.putpixel((8,60),(0, 0, 0, 0))
                img.putpixel((9,60),(0, 0, 0, 0))
                img.putpixel((10,60),(0, 0, 0, 0))
                img.putpixel((11,60),(0, 0, 0, 0))
                img.putpixel((12,60),(0, 0, 0, 0))
                img.putpixel((4,61),(0, 0, 0, 0))
                img.putpixel((5,61),(0, 0, 0, 0))
                img.putpixel((6,61),(0, 0, 0, 0))
                img.putpixel((8,61),(0, 0, 0, 0))
                img.putpixel((9,61),(0, 0, 0, 0))
                img.putpixel((11,61),(0, 0, 0, 0))
                img.putpixel((12,61),(0, 0, 0, 0))
                img.putpixel((13,61),(0, 0, 0, 0))
                img.putpixel((4,62),(0, 0, 0, 0))
                img.putpixel((5,62),(0, 0, 0, 0))
                img.putpixel((8,62),(0, 0, 0, 0))
                img.putpixel((9,62),(0, 0, 0, 0))
                img.putpixel((10,62),(0, 0, 0, 0))
                img.putpixel((12,62),(0, 0, 0, 0))
                img.putpixel((13,62),(0, 0, 0, 0))
                img.putpixel((3,63),(0, 0, 0, 0))
                img.putpixel((4,63),(0, 0, 0, 0))
                img.putpixel((8,63),(0, 0, 0, 0))
                img.putpixel((9,63),(0, 0, 0, 0))
            # Health
            img.putpixel((71,0),(0, 0, 0, 0))
            img.putpixel((72,0),(0, 0, 0, 0))
            img.putpixel((73,0),(0, 0, 0, 0))
            img.putpixel((74,0),(0, 0, 0, 0))
            img.putpixel((75,0),(0, 0, 0, 0))
            img.putpixel((76,0),(0, 0, 0, 0))
            img.putpixel((77,0),(0, 0, 0, 0))
            img.putpixel((78,0),(0, 0, 0, 0))
            img.putpixel((79,0),(0, 0, 0, 0))
            img.putpixel((80,0),(0, 0, 0, 0))
            img.putpixel((81,0),(0, 0, 0, 0))
            img.putpixel((82,0),(0, 0, 0, 0))
            img.putpixel((83,0),(0, 0, 0, 0))
            img.putpixel((72,1),(0, 0, 0, 0))
            img.putpixel((73,1),(0, 0, 0, 0))
            img.putpixel((74,1),(0, 0, 0, 0))
            img.putpixel((75,1),(0, 0, 0, 0))
            img.putpixel((76,1),(0, 0, 0, 0))
            img.putpixel((77,1),(0, 0, 0, 0))
            img.putpixel((78,1),(0, 0, 0, 0))
            img.putpixel((79,1),(0, 0, 0, 0))
            img.putpixel((80,1),(0, 0, 0, 0))
            img.putpixel((81,1),(0, 0, 0, 0))
            img.putpixel((82,1),(0, 0, 0, 0))
            img.putpixel((74,2),(0, 0, 0, 0))
            img.putpixel((75,2),(0, 0, 0, 0))
            img.putpixel((76,2),(0, 0, 0, 0))
            img.putpixel((77,2),(0, 0, 0, 0))
            img.putpixel((78,2),(0, 0, 0, 0))
            img.putpixel((79,2),(0, 0, 0, 0))
            img.putpixel((80,2),(0, 0, 0, 0))
            img.putpixel((75,3),(0, 0, 0, 0))
            img.putpixel((76,3),(0, 0, 0, 0))
            img.putpixel((77,3),(0, 0, 0, 0))
            img.putpixel((78,3),(0, 0, 0, 0))
            img.putpixel((79,3),(0, 0, 0, 0))
            img.putpixel((76,4),(0, 0, 0, 0))
            img.putpixel((77,4),(0, 0, 0, 0))
            img.putpixel((78,4),(0, 0, 0, 0))
            img.putpixel((77,5),(0, 0, 0, 0))

    # Save the cropped image in the "Portraits" folder with the same filename
    output_path = os.path.join(output_folder, jpg_file.replace(".jpg", ".png"))
    img.save(output_path)

    print(f"Cropped image saved: {output_path}")