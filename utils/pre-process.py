import cv2
import numpy as np
from math import *


def seperateImage(img):
    b, g, r = cv2.split(img)
    return b,g,r

def writeImage(img,path):
    cv2.imwrite(path,img)

# returns an image after being read
def read(img):
    img = cv2.imread(img)
    return img

##
## TRAINING RESULTS
##
# img = read("/home/nvidia/allen/pytorch_unet_trained/data/train_masks_cotton/0008.jpg")
# colors, counts = np.unique(img.reshape(-1, 3), axis=0, return_counts=True)

# for color, count in zip(colors, counts):
#     print("{} = {} pixels".format(color, count))


# import matplotlib.pyplot as plt #importing matplotlib
# img = plt.imread("/home/nvidia/allen/pytorch_unet_trained/data/train_masks_cotton/0008.jpg")
# plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k') #calculating histogram


import cv2 
  
# importing library for plotting 
import matplotlib
  
# reads an input image 
img = cv2.imread('/home/nvidia/allen/pytorch_unet_trained/data/train_masks_cotton/0008.jpg',0) 
  
# find frequency of pixels in range 0-255 
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
  
# show the plotting graph of an image 
plt.plot(histr) 
plt.show() 



# np.count_nonzero(img == value) can be used in the grayscale case 
# a = np.count_nonzero((img == (0,0,0)).all(axis = 1))
# print("a = ",a)
# # print(b.shape)

# # b,g,r = seperateImage(img)
# # print(b)
# # print(g)
# # print(r)

# # threshold = 150


# ##
# ## TESTING RESULTS
# ##
# img2 = read("/home/nvidia/allen/pytorch_unet_trained/tests_transformed/test_0008.jpg")
# # np.count_nonzero(img == value) can be used in the grayscale case 
# a_test = np.count_nonzero((img2 == (0,0,0)).all(axis = 1))
# print("a_test=",a_test)

# ## error over ground truth 
# difference  = abs(a_test - a)
# error = (float(difference)/a) 

# print("-----------")
# print("difference " + str(difference))
# print("error " +str(error))
# print("-----------")

# b,g,r = seperateImage(img2)
# print(b)
# print(g)
# print(r)

# threshold = 150


# print(b.shape)


# print(img.shape)

    
    
    