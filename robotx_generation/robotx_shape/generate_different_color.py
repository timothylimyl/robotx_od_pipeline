# -*- coding: utf-8 -*-
"""
This script is to generate different colors of shapes as u see fit.

# Initially I only had shape1-4. Shape5-10 is generated.


"""

import cv2


i = 1
image   = cv2.imread('robotx_shape/shape{}.PNG'.format(i))

# If you want to resize the object, uncomment:
'''
width  = 300
height = 300
image   = cv2.resize(image,(width,height),interpolation=cv2.INTER_AREA)
'''

#BGR Channel
blue  = image[:,:,0].copy()
green = image[:,:,1].copy()
red   = image[:,:,2].copy()

#Now change the color (replace the color channel according to what u want):

image[:,:,0]  = red
image[:,:,1]  = green
image[:,:,2]  = blue 

# change it to the next shape, shape_.PNG , fill in with number
cv2.imwrite('shape5.PNG',image)

cv2.imshow('Images',image)
cv2.waitKey(0)
cv2.destroyAllWindows()





