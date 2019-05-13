import cv2
import numpy as np

img = cv2.imread('../images/input.jpg')
cv2.imshow('Original', img)

##########
# Translation

num_rows, num_cols = img.shape[:2]

translation_matrix = np.float32([ [1,0,70], [0,1,110] ])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols + 70, num_rows + 110))
translation_matrix = np.float32([ [1,0,-30], [0,1,-50] ])
img_translation = cv2.warpAffine(img_translation, translation_matrix, (num_cols + 70 + 30, num_rows + 110 + 50))
#cv2.imshow('Translation', img_translation)

##########
# Rotation  

# cropped
rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 1)
img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
#cv2.imshow('Rotation', img_rotation)

# not cropped
translation_matrix = np.float32([ [1,0,int(0.5*num_cols)], [0,1,int(0.5*num_rows)] ])
img_translation = cv2.warpAffine(img, translation_matrix, (2*num_cols, 2*num_rows))

rotation_matrix = cv2.getRotationMatrix2D((num_cols, num_rows), 30, 1)
img_rotation = cv2.warpAffine(img_translation, rotation_matrix, (2*num_cols, 2*num_rows))

#cv2.imshow('Rotation', img_rotation)

##########

# Scaling
img_scaled = cv2.resize(img,None,fx=1.2, fy=1.2, interpolation = cv2.INTER_LINEAR)
cv2.imshow('Scaling - Linear Interpolation', img_scaled)
img_scaled = cv2.resize(img,None,fx=1.2, fy=1.2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', img_scaled)
img_scaled = cv2.resize(img,(450, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', img_scaled)

cv2.waitKey()
