import cv2
import numpy as np

img = cv2.imread('../images/IMG_2374.jpg')
rows, cols = img.shape[:2]

#src_points = np.float32([[0,0], [cols-1,0], [0,rows-1], [cols-1,rows-1]])
#dst_points = np.float32([[0,0], [cols-1,0], [int(0.33*cols),rows-1], [int(0.66*cols),rows-1]]) 
#src_points = np.float32([[0,0], [0,rows-1], [cols/2,0], [cols/2,rows-1]])
#dst_points = np.float32([[0,100], [0,rows-101], [cols/2,0], [cols/2,rows-1]])
src_points = np.float32([[261,1064], [1598,847], [1201,2218], [3087,1583]])
dst_points = np.float32([[0,0], [480,0], [0,640], [480,640]])

projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

img_output = cv2.warpPerspective(img, projective_matrix, (480,640))

#cv2.imshow('Input', img)
cv2.imshow('Output', img_output)
cv2.waitKey()
