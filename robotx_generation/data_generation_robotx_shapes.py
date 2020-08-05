'''
Author: Timothy Lim

Purpose: Script generates image data for shapes in RobotX Competition namely
cruciform, triangles and circle. Background images used are sky and ocean. The shapes
are taken from robotx videos and cropped into backgrounds.

The data will then be used to train a 2D Object Detection Algorithm.

** You'll need to manually change to shapes images that u want and move it 
   positions you want to overlay in the backgroundf image. 

'''

import cv2

# Background image size:
width  = 1200
height = 800
img_per_background = 1 # Number of images per background


'''
Instructions:
    
1. Change variable x,y,z according to which 3 shapes u want to use for each background images.
   ( There's currently 32 background to choose from and 10 shapes)
2. Change the number of background images u want to overlay as u see fit
3. Change the position of overlaying (line64-)
4. After running once and generating data, change the name of files before generating next batch.
5. Repeat 1-4.

Tip1: if u want to use background 10 onwards, change b_start =10
Tip2: cv2.imwrite will overwrite your images of same filename. 
      use this feature and open robotx_shape_generated folder to eyeball
      the positions of shape generated and change as u see fit.

'''
b_start      = 1 # ranging from 1 to 32-n_background.
n_background = 10 # Number of background images

x = 3
y = 8
z = 4


j = 0
for i in range(b_start,b_start+n_background):

    image   = cv2.imread('background/{}.jpg'.format(i))
    image   = cv2.resize(image,(width,height),interpolation=cv2.INTER_AREA)
    
    for _ in range(img_per_background):
        
        img = image.copy()
        shape1   = cv2.imread('robotx_shape/shape{}.PNG'.format(x))
        shape2   = cv2.imread('robotx_shape/shape{}.PNG'.format(y))
        shape3   = cv2.imread('robotx_shape/shape{}.PNG'.format(z))

        shapeimg1 = shape1.copy()
        shapeimg2 = shape2.copy()
        shapeimg3 = shape3.copy()

        
        # overlay shapes 
        
        x1,y1 = shapeimg1.shape[0:2]
        x2,y2 = shapeimg2.shape[0:2]
        x3,y3 = shapeimg3.shape[0:2]

        # Change the positions here:
        img[400:400+x1,550:550+y1,:]   =  shapeimg1
        img[200:200+x2,100:100+y2,:]   =  shapeimg2
        img[400:400+x3,900:900+y3,:]   =  shapeimg3
        
        # Remember to change the name ____.jpg everytime u want to generate
        # next batch of images by filling in the new name ___{}.jpg.
        
        cv2.imwrite('robotx_shape_generated/o{}.jpg'.format(j),img)
        
        j+=1
        

