

import os
import numpy as np
from PIL import Image

def get_rgb(image_path):
    """Extract the average RGB color of a given image."""
    img = Image.open(image_path)
    img_array = np.array(img)
    average_color = np.mean(img_array[:, :, :3], axis=(0, 1))
    return average_color

def classify_image(rgb_values, thresholds=(128, 128, 128)):
    """Classify the image based on predefined RGB thresholds."""
    r, g, b = rgb_values
    threshold_r, threshold_g, threshold_b = thresholds
    if r > threshold_r and r > g and r > b:
        return 'Red'
    elif g > threshold_g and g > r and g > b:
        return 'Green'
    elif b > threshold_b and b > r and b > g:
        return 'Blue'
    else:
        return 'Unclassified'

def get_image_paths(directory):
    """Retrieve a list of image file paths from the specified directory and its subdirectories."""
    image_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".jpg", ".png")):
                image_path = os.path.join(root, file)
                image_paths.append(image_path)
    return image_paths

def main(directory_path):
    image_paths = get_image_paths(directory_path)
    color_counts = {'Red': 0, 'Green': 0, 'Blue': 0, 'Unclassified': 0}

    for image_path in image_paths:
        rgb_values = get_rgb(image_path)
        color_class = classify_image(rgb_values)
        color_counts[color_class] += 1
        print(f"Image: {image_path.split('/')[-1]}, Classified as: {color_class}")

    print("Color counts:", color_counts)

if __name__ == '__main__':
    directory_path = "./training_data/"
    main(directory_path)
