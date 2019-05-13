import cv2

img = cv2.imread('../images/input.jpg')

# Original image
cv2.imshow('Original image', img)

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale image', gray_img)

# Convert to YUV 
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow('YUV image', yuv_img)

# Displaying the channels of YUV separately
#cv2.imshow('Y channel', yuv_img[:,:,0])
#cv2.imshow('U channel', yuv_img[:,:,1])
#cv2.imshow('V channel', yuv_img[:,:,2])

# Convert to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image', hsv_img)

# Displaying the channels of HSV separately
cv2.imshow('H channel', hsv_img[:,:,0])
cv2.imshow('S channel', hsv_img[:,:,1])
cv2.imshow('V channel', hsv_img[:,:,2])

cv2.waitKey()
