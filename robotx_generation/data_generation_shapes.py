'''
Author: Timothy Lim

Purpose: Script generates image data for shapes in RobotX Competition namely
cruciform, triangles and circle. Background images used are sky and ocean.

The data will then be used to train a 2D Object Detection Algorithm. 

'''

# We will generate 256 images using 32 backgrounds. Each background will have 
# 5 different images, with altering color and position of objects of interest.
# There will be some shapes overlay. Data should be inspected before use.
# Total images generated = 32*5 = 160


# Sometimes shape overlay, delete those.

# In the 2D Object Detection pipeline, the images will be augmented, increasing by 
# threefold.

import cv2
import numpy as np
import random

width  = 1200
height = 800
n_background = 32 # Number of background images
img_per_background = 5 # Number of images per background
j = 1

for i in range(1,n_background+1):
    
    # Reading background images and resizing.
    image   = cv2.imread('background/{}.jpg'.format(i))
    image   = cv2.resize(image,(width,height),interpolation=cv2.INTER_AREA)
    
    for _ in range(img_per_background):
        
        # Copy image array:
        img =  np.copy(image)
        
        # Randomly change color:
        R = int(random.uniform(0,1) * 255)
        G = int(random.uniform(0,1) * 255)
        B = int(random.uniform(0,1) * 255)
        
        # Randomly change position in images:
        # Circle:
        circleX = int(width  * random.uniform(0.2,1))
        circleY = int(height * random.uniform(0.2,1))
        circleSize = int(random.uniform(0.35,1)*100)
        
        # Triangle:
        topX  = int(width*random.uniform(0.4,0.9))
        topY  = int(height*random.uniform(0.4,0.9))
        triHeight = int(random.uniform(40,160))
        btmY  = int(topY + triHeight)
        triWidth = int(140*random.uniform(0.3,1))
        btmX1 = topX - triWidth 
        btmX2 = topX + triWidth
        triangle = np.array([[topX,topY],[btmX1,btmY],[btmX2,btmY]], np.int32)  
        
        # Cruciform:
        crossSize  = int(random.uniform(8,15))
        x_constant = int(random.uniform(0.1*width,0.8*width))
        y_constant = int(random.uniform(0.1*height,0.8*height))

        length     = int(random.uniform(40,120))
        y1 = y_constant + length
        y2 = y_constant - length
        x1 = x_constant - length
        x2 = x_constant + length
        
        
        ## Adding Shapes to image copy:
        # Circle:
        cv2.circle(img,(circleX,circleY),circleSize,(B,G,R),-1)
        # Triangle:
        cv2.fillPoly(img, [triangle], (R,G,B))
        # Cruciform:
        cv2.line(img,(x_constant,y1),(x_constant,y2),(R,R,G),crossSize)
        cv2.line(img,(x1,y_constant),(x2,y_constant),(R,R,G),crossSize)
        
        # Saving image:
        cv2.imwrite('generated/image{}.jpg'.format(j),img)
        
        j += 1
    
    

#cv2.imwrite('generated_image.png',img)
        
'''
cv2.imshow('Images',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''