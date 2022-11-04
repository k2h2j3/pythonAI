import numpy as np
from keras import Sequential
from keras.datasets import cifar10
from keras.utils import np_utils
from keras.layers.core import Dense,Dropout,Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
IMG_X, IMG_Y, IMG_CH = x_train.shape[1], x_train.shape[2], x_train.shape[3]

#print(x_train.shape, y_train.shape)
#print(x_test.shape, y_test.shape)

#step1. 원핫인코딩

x_train = x_train.astype(np.float32) / 255
x_test = x_test.astype(np.float32) / 255
cifar10_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truct']
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

#print(x_test.shape, y_test.shape)

#step2. 모델 생성

model = Sequential()
model.add(Conv2D(filters=32, input_shape=(IMG_X, IMG_Y, IMG_CH),
kernel_size=(3,3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(units=512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=10, activation='softmax'))
model.summary()

#step3. 모델 학습

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x=x_train, y=y_train, batch_size=128, epochs=2, validation_split=0.2)
scores = model.evaluate(x=x_test, y=y_test, batch_size=128)
print(scores)

# step 4. 예측값 출력 및 학습된 모델 저장
results = model.predict(x_test[:1])
print(cifar10_classes[np.argmax(results[0])])
model.save('cifar10.h5')






