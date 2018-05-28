from keras.models import load_model
import selenium
from mss import mss
import cv2
import numpy as np

model = load_model('./network/dino_ai_weights_post_train.h5')

def predict(game_element, frame):

    # configuration for image capture
    sct = mss()
    coordinates = {
        'top': 180,
        'left': 315,
        'width': 615,
        'height': 160,
    }

    # image capture
    img = np.array(sct.grab(coordinates))

    # cropping, edge detection, resizing to fit expected model input
    img = img[::,75:615]
    img = cv2.Canny(img, threshold1=100, threshold2=200)
    cv2.imwrite('game_frame_{0}.jpg'.format(frame), img)

    img = cv2.imread('game_frame_{0}.jpg'.format(frame), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    img = img[np.newaxis, :, :, np.newaxis]
    img = np.array(img)

    # model prediction
    y_prob = model.predict(img)
    prediction = y_prob.argmax(axis=-1)

    if prediction == 1:
        game_element.send_keys(u'\ue013')
    if prediction == 0:
        pass
    if prediction == 2:
        game_element.send_keys(u'\ue015')

