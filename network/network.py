import keras
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import preprocessing
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
        img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
        img = img[:, :, np.newaxis]
        all_images.append(img)
        img_num += 1

X = np.array(all_images)

print(X[0].shape)

# split into test and train set
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.2, random_state=5)

## input image dimensions
img_x, img_y = 80, 270
input_shape = (img_x, img_y, 1)

# convert class vectors to binary class matricies for use in catagorical_crossentropy loss below
# number of action classifications
classifications = 3
y_train = keras.utils.to_categorical(y_train, classifications)
y_test = keras.utils.to_categorical(y_test, classifications)

# CNN model
model = Sequential()
model.add(Conv2D(100, kernel_size=(2, 2), strides=(2, 2), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(250, activation='relu'))
model.add(Dense(classifications, activation='softmax'))
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=['accuracy'])

# tensorboard data callback
tbCallBack = keras.callbacks.TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)

model.fit(x_train, y_train, batch_size=250, epochs=60, validation_data=(x_test, y_test), callbacks=[tbCallBack])

# save weights post training
model.save('dino_ai_weights_post_train_2.h5')
