import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn import preprocessing
import os
from skimage import io
import cv2

# seed weights
np.random.seed(3)

X = []
Y = []

with open ('../actions.csv', 'r') as f:
    for line in f:
        Y.append(line.rstrip())


all_images = []
img_num = 0
while img_num < 1567:
        img = cv2.imread(r'../images/frame_{0}.jpg'.format(img_num), cv2.IMREAD_GRAYSCALE)
        img = img[:, :, np.newaxis]
        all_images.append(img)
        img_num += 1

X = np.array(all_images)

# split into test and train set
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.2, random_state=5)

## input image dimensions
img_x, img_y = 160, 540
input_shape = (img_x, img_y, 1)

# convert class vectors to binary class matricies for use in catagorical_crossentropy loss below
# number of action classifications
classifications = 3
y_train = keras.utils.to_categorical(y_train, classifications)
y_test = keras.utils.to_categorical(y_test, classifications)

# CNN model
model = Sequential()
model.add(Conv2D(128, kernel_size=(2, 2), strides=(1, 1), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(256, (2, 2), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dense(classifications, activation='softmax'))

model.compile(loss="categorical_crossentropy",optimizer="adam", metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=128, epochs=50, validation_data=(x_test, y_test))