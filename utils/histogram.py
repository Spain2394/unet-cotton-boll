# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image

plot_lines = []

gtruth_image = cv2.imread('/Volumes/Elements/midterm/unet-cotton-boll/data/train_masks_cotton/0011.jpg',0)

validation_image = cv2.imread('/Volumes/Elements/midterm/unet-cotton-boll/data/tests_transformed/test_0011.jpg',0)

# find frequency of pixels in range 0-255
gtruth_histr = cv2.calcHist([gtruth_image],[0],None,[256],[0,256])
validation_histr = cv2.calcHist([validation_image],[0],None,[256],[0,256])

diff_hist = validation_histr-gtruth_histr

# pyplot.hist(x, bins, alpha=0.5, label='x')
# pyplot.hist(y, bins, alpha=0.5, label='y')
# pyplot.legend(loc='upper right')

l1 = plt.plot(diff_hist, '-',color='black',label='delta')
l2 = plt.plot(gtruth_histr, '-',color='green',label='ground truth')
l3 = plt.plot(validation_histr,'--',color='red',label='prediction')

# legend = plt.legend(l1, l2)
plt.legend(loc='upper right')
plt.xlabel('Color value')
plt.ylabel('Frequency')
plt.title("Pixel Color Appearance")
plt.show()



# # show the plotting graph of an image
# plt.plot(histr)
# plt.show()
