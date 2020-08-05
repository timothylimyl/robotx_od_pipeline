'''

Author: Timothy Lim
Purpuse: This script is written to visualise generated images.

'''

import cv2
import numpy as np


image   = cv2.imread('robotx_shape_generated/a{}.jpg'.format(2))
image1   = cv2.imread('robotx_shape_generated/b{}.jpg'.format(1))
image2  = cv2.imread('robotx_shape_generated/k{}.jpg'.format(6))
image3   = cv2.imread('robotx_shape_generated/g{}.jpg'.format(5))



image4   = cv2.imread('generated/image{}.jpg'.format(9))
image5   = cv2.imread('generated/image{}.jpg'.format(21))
image6   = cv2.imread('generated/image{}.jpg'.format(7))
image7   = cv2.imread('generated/image{}.jpg'.format(45))

new1 = np.hstack((image,image1))
new2 = np.hstack((image2,image3))

new3 = np.hstack((image4,image5))
new4 = np.hstack((image6,image7))


stack1 = np.vstack((new1,new2))
stack2 = np.vstack((new3,new4))

final_img = np.hstack((stack1,stack2))

width  = 1000
height = 600
image   = cv2.resize(final_img,(width,height),interpolation=cv2.INTER_AREA)


cv2.imwrite('generated_image.jpg',final_img)

'''
cv2.imshow('Images',final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''