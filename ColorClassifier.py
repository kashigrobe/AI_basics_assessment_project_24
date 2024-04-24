

import os
import numpy as np
from PIL import Image

def get_rgb(image_path):
    """Extract the average RGB color of a given image."""
    img = Image.open(image_path)
    img_array = np.array(img)
    average_color = np.mean(img_array[:, :, :3], axis=(0, 1))
    return average_color

def classify_image(rgb_values):
    """Classify the image based on a set of rules for RGB value dominance and edge cases."""
    r, g, b = rgb_values
    min_threshold = 50  # Minimum difference to consider a color dominant
    grey_scale_threshold = 15  # Maximum difference between values to consider the color as grey
    
    # Check if the color is nearly grey/neutral
    if max(abs(r - g), abs(r - b), abs(g - b)) < grey_scale_threshold:
        return 'Grey/Neutral'
    
    # Dominance check with adjusted thresholds
    dominant_threshold = max(r, g, b) * 0.9  # 90% of the max value
    
    # Determine which is the dominant color
    if r > dominant_threshold and r > g + min_threshold and r > b + min_threshold:
        return 'Red'
    elif g > dominant_threshold and g > r + min_threshold and g > b + min_threshold:
        return 'Green'
    elif b > dominant_threshold and b > r + min_threshold and b > g + min_threshold:
        return 'Blue'
    
    # Check for mixed colors
    if r > dominant_threshold and g > dominant_threshold:
        return 'Orange/Yellow (Red/Green Mix)'
    if r > dominant_threshold and b > dominant_threshold:
        return 'Purple (Red/Blue Mix)'
    if g > dominant_threshold and b > dominant_threshold:
        return 'Cyan (Green/Blue Mix)'
    
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
    # Update the dictionary to include all categories returned by the classify_image function
    color_counts = {
        'Red': 0,
        'Green': 0,
        'Blue': 0,
        'Grey/Neutral': 0,
        'Orange/Yellow (Red/Green Mix)': 0,
        'Purple (Red/Blue Mix)': 0,
        'Cyan (Green/Blue Mix)': 0,
        'Unclassified': 0
    }

    for image_path in image_paths:
        rgb_values = get_rgb(image_path)
        color_class = classify_image(rgb_values)
        if color_class not in color_counts:  # Additional check for safety
            color_counts[color_class] = 0
        color_counts[color_class] += 1
        print(f"Image: {image_path.split('/')[-1]}, RGB: {rgb_values}, Classified as: {color_class}")

    print("Color counts:", color_counts)


if __name__ == '__main__':
    directory_path = "./training_data/"
    main(directory_path)
