import cv2
import numpy as np

test_image = cv2.imread(image.jpg)
cv2.imshow("Before", test_image)
Brightness_Matrix = np.ones(test_image.shape, dtype ="uint8") *50
print(Brightness_Matrix)
brightened_image =cv2.add(test_image, Brightness_Matrix)
cv2.imshow("After", brightened_image)
cv2,waitkey(0)
cv2.destroyAllWindows(0)
