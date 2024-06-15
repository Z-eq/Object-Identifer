from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(640, 640)):
    """
    Resize all images in the input folder to the target size and save them in the output folder.
    :param input_folder: Path to the folder containing original images.
    :param output_folder: Path to the folder where resized images will be saved.
    :param target_size: Tuple (width, height) for the desired image size.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)
            img_resized = img.resize(target_size, Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)
            print(f"Resized {filename} to {target_size}")

# Example usage:
input_folder_path = "/home/data/Videos/park-analyzer/dataset/images/all"
output_folder_path = "/home/data/Videos/park-analyzer/dataset/images/all/11"
resize_images(input_folder_path, output_folder_path)

