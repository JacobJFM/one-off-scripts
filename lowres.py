import os, argparse
from pathlib import Path
from PIL import Image

def is_image_file(filepath):
    # List of common image file extensions
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
    ext = os.path.splitext(filepath)[1].lower()
    
    # Check extension first
    if ext in image_extensions:
        try:
            # Attempt to open with PIL to confirm it's a valid image
            with Image.open(filepath) as img:
                img.verify()  # This checks if the file is an image without fully loading it
            return True
        except (OSError, Image.UnidentifiedImageError):
            return False
    return False

# folder = 'images'
# new_dimension = (width, height)
def resize(folder, target_width, target_height, new_subdir):
    images_folder = Path(folder)
    for child in images_folder.iterdir():
        if not is_image_file(child):
            continue
        print("Found image:", child)
        image_path = child.absolute()

        image = Image.open(image_path)
        src_width, src_height = image.size
        
        # calculate scaling factor
        width_scale = target_width / src_width
        height_scale = target_height / src_height
        scale = min(width_scale, height_scale)

        # calculate new image dimensions
        new_width = int(src_width * scale)
        new_height = int(src_height * scale)

        # resize image
        resized_image = image.resize((new_width, new_height)) 

        # create if the subdir not exists
        subdir = images_folder.joinpath(new_subdir)
        if not subdir.exists():
            subdir.mkdir(parents=True, exist_ok=True)
        
        to_path = subdir.joinpath(child.name)  # join adds the path-separators
        print("Saving resized image to:", to_path)
        resized_image.save(to_path)  # could also add save-options like 'JPEG', quality=90

parser = argparse.ArgumentParser()
parser.add_argument('folder', help='source folder')
parser.add_argument('width', help='target width', type=float)
parser.add_argument('height', help='target height', type=float)
parser.add_argument('subdirectory', help='new subdirectory', nargs='?', default='lowres')
args = parser.parse_args()

resize(args.folder, args.width, args.height, args.subdirectory)