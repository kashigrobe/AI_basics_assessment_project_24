import os
import numpy as np
from PIL import Image, ImageDraw

def create_gradient_image(color1, color2, width, height):
    """Generate a horizontal gradient between two RGB tuples."""
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (x / width)) for x in range(width)])  # horizontal gradient
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def generate_and_classify_gradients(directory):
    colors = {
        'Red': [(255, 0, 0), (128, 0, 0)],
        'Green': [(0, 255, 0), (0, 128, 0)],
        'Blue': [(0, 0, 255), (0, 0, 128)]
    }
    for color_name, (color1, color2) in colors.items():
        for i in range(1, 4):  # Generate 3 images per color
            img = create_gradient_image(color1, color2, 100, 100)
            img_path = os.path.join(directory, color_name, f"{color_name}_gradient_{i}.png")
            os.makedirs(os.path.dirname(img_path), exist_ok=True)
            img.save(img_path)
            rgb_values = get_rgb(img_path)
            color_class = classify_image(rgb_values)
            color_counts[color_class] += 1
            print(f"Generated Image: {img_path}, RGB: {rgb_values}, Classified as: {color_class}")

def get_rgb(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    average_color = np.mean(img_array[:, :, :3], axis=(0, 1))
    return average_color

def classify_image(rgb_values):
    r, g, b = rgb_values
    min_threshold = 50
    grey_scale_threshold = 15
    if max(abs(r - g), abs(r - b), abs(g - b)) < grey_scale_threshold:
        return 'Grey/Neutral'
    dominant_threshold = max(r, g, b) * 0.9
    if r > dominant_threshold and r > g + min_threshold and r > b + min_threshold:
        return 'Red'
    elif g > dominant_threshold and g > r + min_threshold and g > b + min_threshold:
        return 'Green'
    elif b > dominant_threshold and b > r + min_threshold and b > g + min_threshold:
        return 'Blue'
    if r > dominant_threshold and g > dominant_threshold:
        return 'Orange/Yellow (Red/Green Mix)'
    if r > dominant_threshold and b > dominant_threshold:
        return 'Purple (Red/Blue Mix)'
    if g > dominant_threshold and b > dominant_threshold:
        return 'Cyan (Green/Blue Mix)'
    return 'Unclassified'

def get_image_paths(directory):
    image_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".jpg", ".png")):
                image_paths.append(os.path.join(root, file))
    return image_paths

def main(directory_path):
    global color_counts
    color_counts = {'Red': 0, 'Green': 0, 'Blue': 0, 'Grey/Neutral': 0,
                    'Orange/Yellow (Red/Green Mix)': 0, 'Purple (Red/Blue Mix)': 0,
                    'Cyan (Green/Blue Mix)': 0, 'Unclassified': 0}
    generate_and_classify_gradients(directory_path)  # Generate and classify synthetic images
    image_paths = get_image_paths(directory_path)
    for image_path in image_paths:
        rgb_values = get_rgb(image_path)
        color_class = classify_image(rgb_values)
        color_counts[color_class] += 1
        print(f"Image: {image_path.split('/')[-1]}, RGB: {rgb_values}, Classified as: {color_class}")

    print("Color counts:", color_counts)

if __name__ == '__main__':
    directory_path = "./training_data/"
    main(directory_path)
