import cv2
from mss import mss
import numpy as np


def start():
    coordinates = {
        'top': 180,
        'left': 315,
        'width': 615,
        'height': 160,
    }

    sct = mss()

    while True:
        img = np.array(sct.grab(coordinates))
        cv2.imshow('dino', np.array(img))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
