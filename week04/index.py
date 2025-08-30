import cv2
import numpy as np

img = cv2.imread('week04/img1.png')
# img it's the variable named
# get the image for reading

if img is None:
    print('Image not found, Could you checking the path of images')
    exit()
# if image not found, showed print text & exit the program

kernel = np.array([[0, -1, 0],
[-1, 5, -1],
[0, -1, 0]])
# Include kernel with 3x3 to adjust the image to blur & brightness

sharpened = cv2.filter2D(img, -1, kernel)
# sharpened it's keep the value of filter2D of image to make a kernel 3x3

cv2.imshow('Sharpened Image', sharpened)
# Show an image as import 
cv2.waitKey(0)
# waiting key for any press button for....
cv2.destroyAllWindows()
# close the program