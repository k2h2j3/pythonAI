import math
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers.rnn import SimpleRNN, LSTM
from keras.layers.core import Dense

def deg2rad(deg):
    return deg / 180 * math.pi

value = []

for deg in range(0,1440):
    value.append(math.sin(deg2rad(deg/4)))

x_train = []
y_train = []

# step 1. 데이터셋 준비

SEQ_LENGTH = 40
N_FEATURE = 1
for i in range(0,1440-SEQ_LENGTH):
    x_train.append(value[i:i+SEQ_LENGTH])
    y_train.append(value[i+SEQ_LENGTH])

x_train = np.array(x_train)
y_train = np.array(y_train)

print(x_train.shape)
print(y_train.shape)

# step 2. 모델 구현
model = Sequential()
model.add(LSTM(units=4, input_shape=(SEQ_LENGTH,N_FEATURE)))
model.add(Dense(units=1))
model.summary()

# step 3. 모델 학습

model.compile(loss='mse', optimizer='adam')
model.fit(x=x_train, y=y_train, batch_size=10, epochs=20)

# step 4. 모델 예측
results = model.predict(x_train)
# 그래프 그려보기
plt.plot(value,'r') # sine 값 계산한 것
plt.plot(results,'b') # 학습 모델을 이용하여 예측한 값
plt.show()