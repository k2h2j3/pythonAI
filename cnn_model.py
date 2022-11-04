import numpy as np
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers.core import Dense, Flatten
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D

EPOCHS = 2
BATCH_SIZE = 128
CLASSES = 10
IMG_ROWS, IMG_COLS, IMG_CHANNELS = 28, 28, 1
INPUT_SHAPE = (IMG_ROWS, IMG_COLS, IMG_CHANNELS)

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.astype(np.float32) / 255
x_test = x_test.astype(np.float32) / 255
x_train =x_train[:,:,:,np.newaxis]
x_test =x_test[:,:,:,np.newaxis]
y_train = np_utils.to_categorical(y_train, CLASSES)
y_test = np_utils.to_categorical(y_test, CLASSES)

model = Sequential()
model.add(Conv2D(filters=20, kernel_size=5, padding='same', input_shape=INPUT_SHAPE, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
model.add(Conv2D(filters=50, kernel_size=5, padding='same', input_shape=INPUT_SHAPE, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
model.add(Flatten())
model.add(Dense(units=500, activation='relu'))
model.add(Dense(units=CLASSES, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_split=0.2)
scores = model.evaluate(x_test, y_test, batch_size=BATCH_SIZE)
print(scores)
# model predict
print(model.predict(x_test[:1]))
print(np.argmax(model.predict(x_test[:1])))