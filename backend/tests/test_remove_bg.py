import pytest
from app.services.remove_bg import remove_background
import os

def test_remove_bg():
    input_file = "test_images/test_image.png"  # Add a test image in this path
    output_file = "test_images/processed_image.png"
    
    remove_background(input_file, output_file)
    assert os.path.exists(output_file)
