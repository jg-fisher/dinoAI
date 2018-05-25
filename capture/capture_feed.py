import cv2
from mss import mss
import numpy as np

# captures dinosaur run game, designed for my personal computer (adjust coordinates resepctively)
def start():
    """
    Captures video feed frame by frame, crops out unecessary dino and processes
    """

    sct = mss()

    coordinates = {
        'top': 180,
        'left': 315,
        'width': 615,
        'height': 160,
    }

    while True:
        img = np.array(sct.grab(coordinates))

        # crop out the dinosaur from the image array
        img = img[::,75:615]

        # edge detection to reduce amount of image processing work
        img = cv2.Canny(img, threshold1=100, threshold2=200)

        print(img.shape)
        # compress the image dimensions, send it into the network

        # view the network image input
        cv2.imshow('dino', img)

        # break the video feed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
