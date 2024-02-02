# 导入模块
import qrcode
# 传入将要生成二维码的URL
img = qrcode.make('文本内容')
# # 保存
img.save("test.jpg")

import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("test.jpg"))
print("Decoded text is: ", val)
