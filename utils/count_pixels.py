#!/usr/bin/env python3
from PIL import Image
import os
from math import *

## global image number
train_path = '/home/nvidia/allen/pytorch_unet_trained/data/train_masks_cotton/0002.jpg'
im = Image.open(train_path)
print(im)
black = 0
white = 0

for pixel in im.getdata():
    print(pixel)
    if pixel == (255, 255, 255): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
        white += 1
    else:
        black += 1
print(str(train_path) +' black=' + str(black)+', white='+str(white))

# with open("train_metrics.txt", "w") as text_file:
#     print(f'image:' +  str(filename) + 'black=' + str(black)+ ', white='+str(white),file=text_file)


## make me parallel
test_path = '/home/nvidia/allen/pytorch_unet_trained/tests_transformed/test_0002.jpg'
im = Image.open(test_path)
black_t = 0
white_t = 0

for pixel in im.getdata():
    print(pixel)
    if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so

        white_t += 1
    else:
        black_t += 1
print(str(test_path) +' black=' + str(black)+', white='+str(white))


error = white_t-white
# error is different in white pixels over the whole image
print('--------------------------------------------------------------')
print('error=',error)
print('--------------------------------------------------------------')




# with open("test_metrics.txt", "w") as text_file:
#     print(f'image:' +  str(filename) + 'black=' + str(black)+ ', white='+str(white),file=text_file)
