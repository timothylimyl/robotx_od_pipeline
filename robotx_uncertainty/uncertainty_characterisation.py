"""

@author: Tim

Purpose: Take ground truth and predictions from excel file, accumulate 
         midpoint error in x and y direction. 
         Get mean, standard deviation and plot the error distribution
         
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read csv files:
df_truth   = pd.read_csv('test_uncertainty_gt_labels.csv')
df_predict = pd.read_csv('coordinate_predictions.csv')

# Make the ground truth labels of the same formatting as the predictions:

# 1. df_truth needs to rearrange to match df_predict. Put filename in ascending order, then within same filename, xmin has to be sorted. 

df_truth = df_truth.assign(indexNumber=[int(i.split('.')[0]) for i in df_truth['filename']]) # Create a new column with filename as integer for sorting.
df_truth = df_truth.sort_values(['indexNumber','xmin']) # Sort filename then sort within same filename according to xmin (ensure comparing the same bounding boxes)  


# 2. In df_turth, as mentioned in python notebook where we extract the predictions,
#    we have to drop those rows that was not predicted.

# By inspection, I found that Image 24, 25 and 27 has an object that was undetected. 
# Delete the detection of the ground truth for these labels.
df_truth_edited = df_truth[~df_truth['filename'].isin(['24.jpg','25.jpg','27.jpg'])]


# Now we can compare the files but first we need to take the coordinates
# and convert everything into midpoint (x-y) points.

df_truth_xmid = np.array((df_truth_edited['xmax'] + df_truth_edited['xmin'])/2)
df_predict_xmid = np.array((df_predict['xmax'] + df_predict['xmin'])/2)

df_truth_ymid = np.array((df_truth_edited['ymax'] + df_truth_edited['ymin'])/2)
df_predict_ymid = np.array((df_predict['ymax'] + df_predict['ymin'])/2)


# Calculate the error:

error_xmid = df_truth_xmid - df_predict_xmid
error_ymid = df_truth_ymid - df_predict_ymid

# Calculate mean and standard deviation:

mean_x = np.mean(error_xmid)
mean_y = np.mean(error_ymid)
std_x = np.std(error_xmid)
std_y = np.std(error_ymid)

print(f"The mean of x: {mean_x} ,  standard deviation of x: {std_x}")
print(f"The mean of y: {mean_y} ,  standard deviation of y: {std_y}")




n_bins = 30
fig, axs = plt.subplots(1, 2, tight_layout=True)
axs[0].hist(error_xmid, bins=n_bins)
axs[0].set_title('Distribution of error,x-coordinate')
axs[0].set_xlabel('Error (pixel distance)')
axs[0].set_ylabel('Frequency')

axs[1].hist(error_ymid, bins=n_bins)
axs[1].set_title('Distribution of error,y-coordinate')
axs[1].set_xlabel('Error (pixel distance)')
axs[1].set_ylabel('Frequency')

print