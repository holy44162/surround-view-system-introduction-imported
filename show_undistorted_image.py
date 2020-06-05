"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Show all four cameras and their device numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import cv2
import numpy as np
import yaml
from imutils.video import VideoStream


# usb devices of the four cameras
camera_devices = [0, 1, 2, 3]
# intrinsic parameter files of the cameras
camera_files = ["./yaml/front.yaml",
                "./yaml/back.yaml",
                "./yaml/left.yaml",
                "./yaml/right.yaml"]

# added by Holy 2006050822
image_files = ["./yaml/front.png",
                "./yaml/back.png",
                "./yaml/left.png",
                "./yaml/right.png"]
# end of addition 2006050822

# resolution of the video stream
W, H = 640, 480


def main():
    print("[INFO] Preparing camera devices ...")
    # captures = [VideoStream(src=k, resolution=(W, H)).start() for k in camera_devices]

    print("[INFO] loading camera intrinsic files ...")
    undistort_maps = []
    for conf in camera_files:
        with open(conf, "r") as f:
            data = yaml.load(f)

        K = np.array(data["K"])
        D = np.array(data["D"])
        map1, map2 = cv2.fisheye.initUndistortRectifyMap(
            K,
            D,
            np.eye(3),
            K,
            (W, H),
            cv2.CV_16SC2
        )
        undistort_maps.append((map1, map2))

    # put all frames in one window
    corrected = np.zeros((2*H, 2*W, 3), dtype=np.uint8)
    region = {0: corrected[:H, :W],
              1: corrected[:H, W:],
              2: corrected[H:, :W],
              3: corrected[H:, W:]}

    while True:
        print("[INFO] processing camera data ...")
        frames = []
        # added by Holy 2006050822
        for device, imgPathName, (map1, map2) in zip(camera_devices, image_files, undistort_maps):
            frame = cv2.imread(imgPathName, cv2.IMREAD_COLOR)
            frame = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
            cv2.putText(frame, "device: {}".format(device), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
            frames.append(frame)
        # end of addition 2006050822
        # for device, cap, (map1, map2) in zip(camera_devices, captures, undistort_maps):
        #     frame = cap.read()
        #     frame = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
        #     cv2.putText(frame, "device: {}".format(device), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        #     frames.append(frame)

        for i, frame in enumerate(frames):
            region[i][...] = frame

        cv2.imshow("corrected", corrected)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    # for cap in captures:
    #     cap.stop()


if __name__ == "__main__":
    main()
