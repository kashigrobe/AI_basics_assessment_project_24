# Basic Color Classifier


# Create sythetic images for color RED, GREEN, BLUE (RGB), 8bit color depth

Create function to create
- lean red, nothing else
- 80% red, rest random GB parts

Repeat for G and B

# Create function that reads RGB image pixel by pixel and counts pixel colors that are not R, G, B (for every image)

e.g. Image coming in with all pixel being classified as 255, 0, 0 is classified as RED  

Steps
- read image
- calculate total number pixels
- loop over every pixel in the image
- classify
- if pix value is not 255,0,0 count as not color

# create function that lists all images in given folder and returns list of it
# create function for testing classifier e.g. we know we have only RED images in RED folder, therefore all images (100%) should be classified as such. Same for G and B => training

# do the same thing with different images to simulate validation 

# one more time against test folder, with exception that test images are mixed and therefore output of classification should be accordingly


