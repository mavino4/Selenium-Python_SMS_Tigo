import cv2
img = cv2.imread("screenshoot.png")
y, x, h, w = 0, 238, 40, 60
crop_img = img[y:y+h, x:x+w]
cv2.imwrite("test_i/test.png", crop_img)
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)