import cv2
#读取图片
image = cv2.imread("dog.jpg")
#将BGR图像转换为灰度
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#图像反转
inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("原图", image)
cv2.imshow("灰度图像", gray_image)
cv2.imshow("反转图像", inverted_image)
cv2.imshow("铅笔素描", pencil_sketch)
cv2.waitKey(0)
