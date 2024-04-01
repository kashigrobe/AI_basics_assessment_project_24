# RGB Classifier Assessment Project

## Problem Statement 
Develop a simple AI tool that can classify images of clothing items by their primary color (e.g., red, blue, green).


## Basic Level Approach

1. This is an image classification problem where the goal is to identify the primary color of a clothing item from its picture.

1. I'm using a basic color histogram analysis to identify the most dominant color in the image, mapping it to predefined color categories.

### Implementation Details
Before implementing this using ML, I want to understand the basics e.g. image resolution versus number of pixels, clustering pixel values into groups, values to histograms and related python funcions and libs.

## Algorithm Selection
- Instead of a complex machine learning model, start with a straightforward approach using color histogram analysis to classify the image based on the most prevalent color pixel in the clothing item.

## Tuning and Evaluation 
- Initially, define a simple palette of colors (e.g., basic colors like red, blue, yellow) and categorize clothing items accordingly. Use a set of clothing images to test and refine the color mapping, ensuring that most items are classified into the correct color category.


## Implementing using ML

### Data & Structure
I'm going to use a supervised approach, providing labled data to the algo. The labeling is done by putting colored images into one of the three (red, green, blue) folders.

### modeling