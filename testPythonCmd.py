"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Show all four cameras and their device numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import cv2
import numpy as np
import yaml
from imutils.video import VideoStream


# # usb devices of the four cameras
# camera_devices = [0, 1, 2, 3]
# # intrinsic parameter files of the cameras
# camera_files = ["./yaml/front.yaml",
#                 "./yaml/back.yaml",
#                 "./yaml/left.yaml",
#                 "./yaml/right.yaml"]

# added by Holy 2006050822
image_files = ["./yaml/front.png",
                "./yaml/back.png",
                "./yaml/left.png",
                "./yaml/right.png"]

img = cv2.imread(image_files[0], cv2.IMREAD_COLOR)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# end of addition 2006050822

W, H = 9, 7
corrected = np.zeros((2*H, 2*W, 3), dtype=np.uint8)
region = {0: corrected[:H, :W],
              1: corrected[:H, W:],
              2: corrected[H:, :W],
              3: corrected[H:, W:]}

print(region[0][...])
