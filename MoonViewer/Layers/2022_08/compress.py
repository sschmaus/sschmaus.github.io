from msilib.schema import Directory
from PIL import Image
import PIL
import os
import glob

def compress_images(directory=False, quality=30):
    # 4. Loop over every image:
    for image in glob.glob(directory, recursive=True):
        print(image)

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        img.save(image, optimize=True, quality=quality)


subdirectory_path = '.\\**\\*.png'
print(subdirectory_path)
compress_images(directory=subdirectory_path)