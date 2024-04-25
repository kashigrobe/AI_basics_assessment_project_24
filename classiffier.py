import os
import cv2
from PIL import Image
import numpy as np

# utiliy functions
def get_images(folder):
    """
    Retrieve a list of image paths from the specified folder.

    Args:
        folder (str): The path to the folder containing the images.

    Returns:
        list: A list of image paths.

    """
    image_paths = []
    for filename in os.listdir(folder):
        if filename.endswith(".png"):
            image_paths.append(os.path.join(folder, filename))
    return image_paths


# classifier training function
def count_images_with_color_threshold(image_paths, target_color, threshold):
    """
    Counts the number of images in the given list of image paths that have a certain number of pixels
    within a specified color threshold.

    Args:
        image_paths (list): A list of file paths to the images.
        target_color (tuple): A tuple representing the target color in RGB format.
        threshold (int): The minimum number of pixels within the color threshold for an image to be counted.

    Returns:
        int: The number of images that meet the specified criteria.
    """
    def is_within_threshold(pixel, target, tol):
        return all(abs(pixel[i] - target[i]) <= tol for i in range(3))
    
    target_r, target_g, target_b = target_color
    tolerance = 10  # You can adjust this to be more or less stringent

    count_images = 0

    for path in image_paths:
        image = Image.open(path)
        image = image.convert('RGB')  # Convert to RGB if not already
        pixels = np.array(image)
        
        match_count = 0
        for row in pixels:
            for pixel in row:
                if is_within_threshold(pixel, (target_r, target_g, target_b), tolerance):
                    match_count += 1

        if match_count > threshold:
            count_images += 1

    return count_images


# classifier function
def RGB_classifier(image_path):
    """
    Classifies an image based on its average color intensity (Red, Green, or Blue).

    Args:
        image_path (str): File path to the image.

    Returns:
        str: The classification of the image as 'Red', 'Green', or 'Blue'.
    """
    image = Image.open(image_path)
    image = image.convert('RGB')

    # loads the RGB values as triplets into a numpy array
    # Here's what the data layout looks like:

    # pixels[y, x, 0] is the Red component of the pixel at position (x, y).
    # pixels[y, x, 1] is the Green component.
    # pixels[y, x, 2] is the Blue component.
    
    pixels = np.array(image)

    # Calculate the mean color in each channel
    mean_colors = np.mean(pixels, axis=(0, 1))

    # Determine which color has the highest average intensity
    if mean_colors[0] > mean_colors[1] and mean_colors[0] > mean_colors[2]:
        return 'Red'
    elif mean_colors[1] > mean_colors[0] and mean_colors[1] > mean_colors[2]:
        return 'Green'
    elif mean_colors[2] > mean_colors[0] and mean_colors[2] > mean_colors[1]:
        return 'Blue'
    else:
        return 'Unclassified'


# main function
if __name__ == "__main__":

    # get list of images from folder red
    imgs = get_images('./data/training/red/')    
    threshold = len(imgs) * 0.8 

# SIMULATED TRAINING RUN     
# FAKE TRAINING FOR LABELED RED COLOR
    # this is only RED
    
    #this is what we are testing for
    #             R   G   B
    color_code = (255, 0, 0)
    result = count_images_with_color_threshold(imgs, color_code, threshold)
    
    print("")
    print("TRAINING ON RED - should return >= 12 equal to 80%")
    if result > threshold:
        print("SUCCESSFULL")
    else:
        print("FAILED")
    
# FAKE TRAINING FOR LABELED GREEN COLOR
    # this is only GREEN
    imgs = get_images('./data/training/green/')
    
    #this is what we are testing for
    #             R   G   B
    color_code = (0, 255, 0)
    result = count_images_with_color_threshold(imgs, color_code, threshold)
    
    print("")
    print("TRAINING ON Green - should return >= 12 equal to 80%")
    if result > threshold:
        print("SUCCESSFULL")
    else:
        print("FAILED")

# FAKE TRAINING FOR LABELED BLUE COLOR
    # this is only BLUE
    imgs = get_images('./data/training/blue/')
    
    #this is what we are testing for
    #             R   G   B
    color_code = (0, 0, 255)
    result = count_images_with_color_threshold(imgs, color_code, threshold)
    
    print("")
    print("TRAINING ON Blue - should return >= 12 equal to 80%")
    if result > threshold:
        print("SUCCESSFULL")
    else:
        print("FAILED")

# DONE TRAINING ---

# SIMULATED VALIDATION


# SIMULATED TESTING
print("==================================================================================")
imgs = get_images('./data/testing/')
for img in imgs:
    result = RGB_classifier(img)
    print(result)
