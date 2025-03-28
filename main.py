import cv2
import numpy as np
 
img = cv2.imread("katsuo.png", cv2.IMREAD_UNCHANGED)
h, w = img.shape[:2]
height, width = 720,1280
background = np.full((height, width, 3),(238,224,173), dtype=np.uint8)
x, y = 10, 0
dx, dy = 5, 2
 
while True:
    frame = background.copy()
    if img.shape[2] == 4:
        alpha = img[:, :, 3] / 255.0
        img_rgb = img[:, :, :3]
        y1, y2 = max(0, y), min(y + h, height)
        x1, x2 = max(0, x), min(x + w, width)
        img_y1, img_y2 = y1 - y, y1 - y + (y2 - y1)
        img_x1, img_x2 = x1 - x, x1 - x + (x2 - x1)
        for c in range(3):
            frame[y1:y2, x1:x2, c] = (
                (1 - alpha[img_y1:img_y2, img_x1:img_x2]) * frame[y1:y2, x1:x2, c] +
                alpha[img_y1:img_y2, img_x1:img_x2] * img_rgb[img_y1:img_y2, img_x1:img_x2, c]
            )
    cv2.imshow("Swimming Katsuo", frame)
 
    x += dx
    y += ((y*100+height)//height)*dy
    if x + w >= width or x <= 0:
        dx = -dx
    if y + h >= height or y <= 0:
        dy = -dy
    if cv2.waitKey(30) & 0xFF == 27:
        break
 
cv2.destroyAllWindows()
