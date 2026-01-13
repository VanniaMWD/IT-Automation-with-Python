#!/usr/bin/env python3

import PIL
#import pillow

from pathlib import Path
from PIL import Image

#script that :
# Iterate through each file in the folder
# For each file:
# 1.-Rotate the image 90° clockwise
# 2.-Resize the image from 192x192 to 128x128
# 3.-Save the image to a new folder in .jpeg format

def process_to_jpeg(source_dir, save_dir):
    path = Path(source_dir)
    dest = Path(save_dir)
    dest.mkdir(parents=True, exist_ok=True)

    counter = 1

    for file in path.iterdir():
        # Only process files and ignore hidden system files
        if file.is_file() and not file.name.startswith('.'):
            try:
                with Image.open(file) as im:
                    # 1. Rotate and Resize
                    # 2. Convert to RGB (Crucial for JPEG)
                    im_processed = im.rotate(90).resize((128, 128)).convert("RGB")
                    
                    # 3. Create new sequential name with .jpeg extension
                    new_filename = f"enhanced_{counter}.jpeg"
                    save_path = dest / new_filename
                    
                    # 4. Save
                    im_processed.save(save_path, "JPEG")
                    
                    print(f"Processed {file.name} -> {new_filename}")
                    counter += 1
            except Exception as e:
                print(f"Could not process {file.name}: {e}")

# Run the function
src = "/home/student"
out = "/opt/icons"
process_to_jpeg(src, out)