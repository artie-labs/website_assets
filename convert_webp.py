import os
from PIL import Image


def convert_images_to_webp(source_directory):
    print('source_directory', source_directory)
    # Walk through all directories and files in source_directory
    for root, dirs, files in os.walk(source_directory):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                # Construct the full file path
                file_path = os.path.join(root, filename)
                # Open the image
                img = Image.open(file_path)
                # Define the output filename with .webp extension
                output_filename = f"{os.path.splitext(filename)[0]}.webp"
                # Save the image in WebP format at the same location
                img.save(os.path.join(root, output_filename), 'WEBP')
                print(f"Converted {filename} to {output_filename} in directory {root}")


if __name__ == "__main__":
    dir = input("Enter the path to the directory containing images: ")
    if not os.path.isabs(dir):
        dir = os.path.abspath(dir)
    convert_images_to_webp(dir)
