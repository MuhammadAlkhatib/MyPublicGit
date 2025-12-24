import numpy as np
import matplotlib as plt
import cv2

img=cv2.imread(r"D:\Downloads\images.jpg")

# cv2.imshow('img',img)
# cv2.waitKey()
# plt.hist(img.ravel(),255,[0,255])
# plt.show()
# equl_img=cv2.equalizeHist(img)
# cv2.imshow('equilized image',equl_img)
# cv2.waitKey()
# plt.hist(equl_img.ravel(),255,[0,255])
# plt.show()

# smooth_img= cv2.medianBlur(img,3)

lap_msk=np.array([[0,-1,0],
                  [-1,4,-1],
                  [0,-1,0]])
lap_img=cv2.filter2D(img,-1 ,lap_msk)

sharpedned_img= cv2.add(img,lap_img)

cv2.imshow('img',img)
cv2.imshow('smooth img',lap_img)
cv2.imshow('sharp img',sharpedned_img)
cv2.waitKey()