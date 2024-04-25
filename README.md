### Color Classifier Project

This document presents a simulated overview of developing a color classifier using a machine learning framework, such as PyTorch or TensorFlow. It describes a typical setup where labeled training data is categorized into directories named after colors (red, green, blue). 

For demonstration we assume the data loading routine in PyTorch would partition the dataset into training and testing subsets, usually with an 80/20 split, to prepare for model training.

Subsequently, we discuss a hypothetical scenario where an image classifier, such as a Convolutional Neural Network (CNN), is designed and executed. This example further assumes that a working model was created and is ready for testing with real-world data.

**Important Note**: When ML modeling it is of critical importance to separate training and testing datasets to prevent data leakage and overfitting.

The classifier, in this narrative, has been constructed during the described training simulations. For illustrative purposes, this example uses the `RGB_Classifier` function to show how the classifier might operate.

For demonstration, three 3x3 pixel images in an 8-bit format are created. These images are used to show typical results: 

Two are expected to be classified as blue and green, while the third might remain unclassified, illustrating a common approach to training and applying a machine learning model in a controlled, educational setting.


## Code 
I'm using a Jupyter Notebook [here...](classy.ipynb)