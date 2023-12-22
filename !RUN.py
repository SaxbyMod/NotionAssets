import os
from PIL import Image

# Define the output folder
output_folder = "Portraits"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the region coordinates
x1, y1 = 130, 270
x2, y2 = 989, 919

# Get a list of PNG files in the current directory
png_files = [file for file in os.listdir() if file.endswith(".png")]

# Process each PNG file
for png_file in png_files:
    # Open the image
    image = Image.open(png_file)

    # Crop the image to the specified region
    cropped_image = image.crop((x1, y1, x2, y2))

    # Save the cropped image in the "Portraits" folder with the same filename
    output_path = os.path.join(output_folder, png_file)
    cropped_image.save(output_path)

    print(f"Cropped image saved: {output_path}")