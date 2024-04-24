# Functions to create images for Blue and Green with similar settings as Red

def create_high_blue_image(index, dimensions=(64, 64), blue_percentage=80):
    num_blue_pixels = int((dimensions[0] * dimensions[1]) * (blue_percentage / 100))
    num_other_pixels = dimensions[0] * dimensions[1] - num_blue_pixels
    
    # Create an image with all pixels initially set to high blue
    image = Image.new('RGB', dimensions, (0, 0, 255))
    pixels = image.load()
    
    # Randomly modify the rest of the pixels to have random red and green parts, but keep blue dominant
    other_pixels = random.sample([(x, y) for x in range(dimensions[0]) for y in range(dimensions[1])], num_other_pixels)
    for x, y in other_pixels:
        # Generate random red and green values
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        pixels[x, y] = (red, green, 255)  # Maintain blue as 255

    # Save the image to a temporary file
    output_path = f'/mnt/data/high_blue_image_{index}.png'
    image.save(output_path)
    return output_path

def create_high_green_image(index, dimensions=(64, 64), green_percentage=80):
    num_green_pixels = int((dimensions[0] * dimensions[1]) * (green_percentage / 100))
    num_other_pixels = dimensions[0] * dimensions[1] - num_green_pixels
    
    # Create an image with all pixels initially set to high green
    image = Image.new('RGB', dimensions, (0, 255, 0))
    pixels = image.load()
    
    # Randomly modify the rest of the pixels to have random red and blue parts, but keep green dominant
    other_pixels = random.sample([(x, y) for x in range(dimensions[0]) for y in range(dimensions[1])], num_other_pixels)
    for x, y in other_pixels:
        # Generate random red and blue values
        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        pixels[x, y] = (red, 255, blue)  # Maintain green as 255

    # Save the image to a temporary file
    output_path = f'/mnt/data/high_green_image_{index}.png'
    image.save(output_path)
    return output_path

# Generate 10 images for each color
training_high_blue_image_paths = [create_high_blue_image(i) for i in range(10)]
training_high_green_image_paths = [create_high_green_image(i) for i in range(10)]

training_high_blue_image_paths, training_high_green_image_paths
