import flwr as fl
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

model = tf.keras.models.Sequential([
    # (None, 28, 28) -> (None, 784)
    tf.keras.layers.Flatten(input_shape=(28, 28), name='input'),
    
    # Layer1: Linear mapping: (None, 784) -> (None, 512)
    tf.keras.layers.Dense(512, name='fc_1'),
    # Activation function: ReLU
    tf.keras.layers.Activation(tf.nn.relu, name='relu_1'),
    
    # Layer2: Linear mapping: (None, 512) -> (None, 256)
    tf.keras.layers.Dense(256, name='fc_2'),
    # Activation function: ReLU
    tf.keras.layers.Activation(tf.nn.relu, name='relu_2'),
    
    # Layer3: Linear mapping: (None, 256) -> (None, 256)
    tf.keras.layers.Dense(256, name='fc_3'),
    # Activation function: ReLU
    tf.keras.layers.Activation(tf.nn.relu, name='relu_3'),
    
    # Layer4: Linear mapping: (None, 256) -> (None, 10)
    tf.keras.layers.Dense(10, name='dense_3'),
    # Activation function: Softmax
    tf.keras.layers.Activation(tf.nn.softmax, name='softmax')
])

# model = tf.keras.applications.MobileNetV2((32, 32, 3), classes=10, weights=None)
model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])

class MNISTClient(fl.client.NumPyClient):
    def get_parameters(self):
        return model.get_weights()

    def fit(self, parameters, config):
        model.set_weights(parameters)
        model.fit(x_train, y_train, epochs=1, batch_size=32, steps_per_epoch=3)
        return model.get_weights(), len(x_train), {}

    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = model.evaluate(x_test, y_test)
        return loss, len(x_test), {"accuracy": accuracy}

fl.client.start_numpy_client("127.0.0.1:8080", client=MNISTClient())