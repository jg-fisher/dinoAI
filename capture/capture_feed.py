import cv2
from mss import mss
import numpy as np
import keyboard

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

    with open('actions.csv', 'w') as csv:
        x = 0
        while True:
            img = np.array(sct.grab(coordinates))

            # crop out the dinosaur from the image array
            img = img[::,75:615]

            # edge detection to reduce amount of image processing work
            img = cv2.Canny(img, threshold1=100, threshold2=200)

            if keyboard.is_pressed('up arrow'): 
                cv2.imwrite('./images/frame_{0}.jpg'.format(x), img)
                csv.write('1\n')
                print('jump write')
                x += 1

            if keyboard.is_pressed('down arrow'):
                cv2.imwrite('./images/frame_{0}.jpg'.format(x), img)
                csv.write('2\n')
                print('duck')
                x += 1

            if keyboard.is_pressed('t'):
                cv2.imwrite('./images/frame_{0}.jpg'.format(x), img)
                csv.write('0\n')
                print('nothing')
                x += 1

            # break the video feed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                csv.close()
                cv2.destroyAllWindows()
                break

