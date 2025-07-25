import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import time

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train / 255.0   # normalization factor
x_test = x_test / 255.0     # normalization factor
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(28,28)),        # input shape
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),  # number of hidden neurons
    tf.keras.layers.Dense(10, activation='softmax')  # number of output neurons
])

model.compile(optimizer='adam',
              loss= tf.keras.losses.CategoricalCrossentropy(from_logits=True), # loss function
              metrics=['accuracy'])

start = time.time()
model.fit(x_train, y_train, epochs=5)
end = time.time()
print(f"TF Training time: ",end - start)       # Output training time
model.evaluate(x_test, y_test)
