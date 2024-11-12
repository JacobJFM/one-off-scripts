# lowres.py
*scale down all images in a folder to a maximum width and height, retaining aspect ratio*

## Dependencies
Other than Python 2.7 or later, the only thing needed is Pillow, which can be installed via pip:
`pip install Pillow`

## Usage
```bash
python lowres.py <source_folder> <width> <height> [subdirectory]
```
* source_folder: The folder containing the images to be downscaled
* width: The maximum width of the output images
* height: The maximum height of the output images
* subdirectory: The name of the subdirectory in which the images will be stored. Defaults to 'lowres' if not specified.


For example, running the script like this:
```bash
python lowres.py media 300 800 small_images
```
would create a subdirectory named "small_images" within the "media" directory, containing downscaled versions of every image at the *top level* of the "media" directory.


Note: images will retain aspect ratio, so each image will be resized depending on 
whether its width or height is the limiting factor. For instance, if the target dimensions are width: 300 and height: 800, an image of size 600x1000 would be downscaled to 300x500, whereas an image of size 600x2400 would be downscaled to 200x800.