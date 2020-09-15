
# Generation of RobotX Data (Images) + Uncertainty Testing

Go over to my google drive for the [full folder](https://drive.google.com/drive/folders/170pHSGsm8GWRfVX1TI-WNVOIN56qY-HT?usp=sharing).

# Data Generation Setup:

#### a. Collecting background images

Get background images from google and stored in the folder `background`.

#### b. nerating shapes on random background

`data_generation_shapes.py` generates shapes of random size on the background images provided. The generated images are stored in the folder `generated`.

#### c. Generating RobotX Shapes on random background

`data_generation_robotx_shapes.py` generates shapes with white background such as those commonly given in the RobotX competition task. I crop out the shapes from competition images and stored them in the folder `robotx_shape`. In `robotx_shape`, I cropped out 4 shapes from RobotX Competition images. I use the script `robotx_shape/generate_different_color.py` to provide me with the more of the same shape with different color. These shapes are all used in  `data_generation_robotx_shapes.py`

#### d. Visualise generated images

The script `visualisation.py` was used to produce a compilation of generated images:

![im](generated_image.jpg)


#### e. Final note

All of the generated images are transfer to the `train` folder in the 2D Object Detection Pipeline and labelled for training.

# Characterising Uncertainty:

#### a. Generating images that are unseen by the training process.

The folder of images can be found in `test_set_uncertainty` which consist of 40 images, each image contains 3 objects of interest.

#### b. Get data on ground truth 

We will need to compare the Ground Truth coordinates of the midpoint of the bounding box versus the coordinates of the predicted. Ground truth coordinates is taken from labelling using `labelImg` and the coordinates information is stored in the folder `test_uncertainty_gt` as `.xml` files. All the ground truth information in `.xml` files are converted to a single `.csv` file using `xml_to_csv.py`.

#### c. Get data on predictions (Inference on trained model)

The model predictions was taken from the [2DOD Pipeline](https://github.com/timothylimyl/robotx_od_pipeline). In the google drive of the pipeline, there is a folder `use_for_inference` which consist of image folders for inference. By running inference through all images from `2DOD_Pipeline/use_for_inference/test_set_uncertainty` by running the script `2DOD_Pipeline/inference_uncertainty.ipynb`, we compiled the bounding box predictions into a `.csv` file `2DOD_Pipeline/use_for_inference/coordinate_predictions.csv`.

**Please read through the inference script `inference_uncertainty.ipynb`, there are written comments there that will help you understand what is the script doing.**


#### d. Computation of error

Now that we have the ground truth and predictions of bounding box position, a script was written to parse the data (`uncertainty/uncertainty_characterisation.py`).  We move the `.csv` files of the ground truth and prediction into the folder `uncertainty`.

By running `uncertainty_characterisation.py`, the script will do a few things for us:

   1. It will properly set up the ground truth bounding box positions to match the bounding box predicted. The ground truth `.csv` has a few issues that we need to deal with first. We need to sort the images in ascending order according to the filename, then we will need to sort it in ascending order according to the minimum x-coordinate value (`xmin`) within the same image to ensure that bounding box coordinates are in the order from left of the image to the right.
   
   2. It finds the midpoint each bounding box.
   
   3. It compares the midpoint of the ground truth label to that of the model prediction.
   
   4. It computes the mean and standard deviation of the error in x and y-axis of the image, and plots a histogram of the error distribution as seen in the Figure below.
   
 ![im2](uncertainty_code_output.jpg)
 
 
 
 
 
 ## Recommendation:
 Please download the folders locally and try everything for yourself.



