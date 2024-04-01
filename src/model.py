import tensorflow as tf

def create_logistic_regression_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=input_shape),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

def make(num_sequences: int, sequence_length: int, embedding_dim: int):
    # Input shape
    input_shape = (num_sequences, sequence_length, embedding_dim)
    model = create_logistic_regression_model(input_shape)
    model.summary()
