### Color Classifier Project

This document presents a simulated approach for the development of a `color classifier`. In a real-life scenario a machine learning framework such as PyTorch or TensorFlow would be used.

I pretended to use `labeled` training data, which is unicolor images, categorized into directories named after the respective colors `(red, green, blue)`. 

The labeled data would be loaded using the data loading routine in PyTorch et al and split into training and validation dataset - usually an 80/20 split is used for model training.

A valid approach for the classifier could be a `Convolutional Neural Network (CNN)`. In this project a much more simple approach is utilized to show the case. The `RGB_classifier`can be found in the `Jupyter Notebook`.

**Important Note**: When ML modeling it is of critical importance to separate training and testing datasets to prevent data leakage and overfitting.


**Let's assume that the classifier has been constructed during the described training.**
The code in the Jupyter notebook shows several scenarios where images are classified into their respective color or tagged as tagged as unclassified.

For sake of simplicty multiple 3x3 pixel images, with an 8-bit color depth have been created via the `create_image` function. Every pixel is represented by an RGB color value triplet e.g. [0, 0, 255] for blue.   

In the test scenario two images are expected to be classified as blue and green, while the third is tagged as unclassified. This scenario simulated the application of the trained model in a real-world scenario.


### High level ML approach
The steps below would usually be done in order to create, validate and test a model.

**Feature Extraction**
- We'll use the image's color data as features. For example, how much red, green, or blue is in an image.

**Model Selection**
- We'll pick an easy-to-understand machine learning model - in this case I created a function.

**Training**
- We will teach the model with some of our images that we already know are red, green, or blue.

**Validation**
- We'll check if our model is learning well by testing it with images it hasn't seen before.

**Tuning**
- If our model isn't smart enough yet, we'll adjust its settings to make it better.

**Evaluation**
- We'll use simple checks, like how often the model is right, to measure how good it is at classifying new images.

**Improvement**
- Depending on how well our model is doing, we might try new techniques or tweak our features to make it even better.


## Code 
```
run pip install -r requirement.txt to install the required libraries
````

All code can be found in the Jupyter Notebook [here...](classifier.ipynb)

## Structure

```
ROOT
|
|-----data
       |------training(labeled data)
                 |--------- blue
                 |--------- green
                 |--------- red
       |   
       |------testing (mixed colors)
```
