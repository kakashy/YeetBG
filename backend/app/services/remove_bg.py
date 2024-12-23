from rembg import remove
from PIL import Image

def remove_background(input_path: str, output_path: str):
    """
    Removes the background from an image and saves the processed image.
    """
    try:
        with open(input_path, "rb") as input_file:
            input_data = input_file.read()
            result = remove(input_data)

        with open(output_path, "wb") as output_file:
            output_file.write(result)
    except Exception as e:
        raise RuntimeError(f"Failed to remove background: {e}")
