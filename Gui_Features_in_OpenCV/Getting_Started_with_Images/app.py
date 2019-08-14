import cv2
import numpy as np

# Load an image in grayscale
img = cv2.imread('../../../_img/terminator_hand.jpg', 0)

# Show the image
cv2.imshow('T-101', img)

# Wait for the user input to continue
# The 0 arg means the program will wait undefinitely for a key
cv2.waitKey(0)

# Close all
cv2.destroyAllWindows()