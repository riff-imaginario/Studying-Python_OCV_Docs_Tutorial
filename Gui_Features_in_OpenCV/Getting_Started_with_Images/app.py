import numpy as np
import cv2


'''
The app is working in a 64-bit system, but if it isn't, try the way of the documentation alert:

Warning -- If you are using a 64-bit machine, you will have to modify k = cv2.waitKey(0) line as follows : k = cv2.waitKey(0) & 0xFF
'''


# Load an image in grayscale
img = cv2.imread('../../../_img/terminator_hand.jpg',0)

# Show the image
cv2.imshow('T-101',img)

# Wait for the user input to continue
# The 0 arg means the program will wait undefinitely for a key
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    # Save a new file
    cv2.imwrite('t-101_gray.png',img)
    cv2.destroyAllWindows()