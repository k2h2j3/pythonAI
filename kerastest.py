import numpy as np
import tensorflow as tf
from keras.layers import Activation, Dropout
from keras.models import Sequential
from keras.layers.core import Dense
from keras.datasets import mnist
from keras.utils import np_utils

(x_train, y_train), (x_test, y_test) = mnist.load_data()
data_size = x_train.shape[1] * x_train.shape[2]
x_train = x_train.reshape(x_train.shape[0], data_size).astype(np.float32)
x_test = x_test.reshape(x_test.shape[0], data_size).astype(np.float32)
x_train = x_train / 255
x_test = x_test / 255
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

NB_CLASSES = 10
model = Sequential()
model.add(Dense(units=128, input_dim=data_size, activation = 'relu'))
model.add(Dropout(0.25))
model.add(Dense(units=128, activation = 'relu'))
model.add(Dropout(0.25))
model.add(Dense(units=10, activation = 'softmax'))

model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=x_train, y=y_train, batch_size=128, epochs=2, validation_split=0.2)

score = model.evaluate(x=x_test, y=y_test, batch_size=128) #모델 평가
print(score)
results = model.predict(x_train[:1])
print(results)


#model = Sequential()
#model.add(Dense(units=4, input_dim=5,activation = 'relu'))
#model.summary()

#print(x_train.shape, x_test.shape)
#print(y_train.shape, y_test.shape)

#print(y_train[0])
#print(y_test[0])


