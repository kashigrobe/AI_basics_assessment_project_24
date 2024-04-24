# RGB Classifier Assessment Project

# RGB Color Classifier Project

## Overview
This project implements a simple RGB color classifier. Given an image, the classifier determines the dominant color among Red, Green, or Blue by analyzing the average RGB values of all pixels.

## Project Structure
- ColorClassifier.py: Main Python script for the RGB color classification.
- `training_data/`: Directory containing training and test images organized by color.
- `RGB_classifier.ipynb`: Jupyter notebook containing the project development and experimental code.
- `README.md`: This file, providing an overview and instructions for the project.

## Usage
To run the classifier, execute the `ColorClassifier.py` script. This script will classify all images in the `training_data` directory and output the classification results to the Terminal.

## How It Works
The `ColorClassifier.py` script contains several functions:
- `get_rgb(image_path)`: Extracts the average RGB values from the specified image.
- `classify_image(rgb_values, thresholds)`: Classifies the image as Red, Green, or Blue based on its average RGB values and given thresholds.
- `get_image_paths(directory)`: Retrieves the paths of all images within the specified directory.
- `main(directory_path)`: The main function that processes the images and prints out the color classification results.

## Requirements
This project requires Python 3 and the following packages:
- `numpy`
- `PIL` (Pillow)

Install the necessary packages using `pip`:
```sh
pip install numpy pillow


## Problem Statement 
I am developing a simple AI tool that can classify images of clothing items by their primary color (e.g., red, blue, green).


## Basic Level Approach

1. This is an image classification problem where the goal is to identify the primary color of a clothing item from its picture.

1. I'm using a basic color histogram analysis to identify the most dominant color in the image, mapping it to predefined color categories.

### Implementation Details
Before implementing this using ML, I want to understand the basics e.g. image resolution versus number of pixels, clustering pixel values into groups, values to histograms and related python funcions and libs like NumPy and PIL (Pillow).

## Algorithm Selection
The project will start with a straightforward color histogram analysis to classify images by the predominant color pixel.

## Tuning and Evaluation 
- First, i will define a simple palette of colors (primary colors: red, blue, yellow) to categorize clothing images.
- Use a set of clothing images to test and refine the color mapping, ensuring that most items are classified into the correct color category.


## Implementing using ML
Upon establishing a baseline with histogram analysis, the following steps will introduce machine learning to enhance the classification accuracy and process scalability:

### Data Pre

### Data & Structure
I'm going to use a supervised approach, providing labeled data to the algo. The labeling is done by putting colored images three separate folders (red, green, blue), which will serve as labeled data for training the algorithm.

### modeling
## Implementing Using Machine Learning
After the initial success with histogram-based classification, we will introduce machine learning to make the tool more precise and capable of handling a larger variety of images.

### Steps for ML Implementation

## Feature Extraction
- We'll use the image's color data as features. For example, how much red, green, or blue is in an image.

## Model Selection
- We'll pick an easy-to-understand machine learning model, like a decision tree or K-Nearest Neighbors, to learn from the color features.

## Training
- We will teach the model with some of our images that we already know are red, green, or blue.

## Validation
- We'll check if our model is learning well by testing it with images it hasn't seen before.

## Tuning
- If our model isn't smart enough yet, we'll adjust its settings to make it better.

## Evaluation
- We'll use simple checks, like how often the model is right, to measure how good it is at classifying new images.

## Improvement
- Depending on how well our model is doing, we might try new techniques or tweak our features to make it even better.
