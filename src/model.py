import tensorflow as tf
import dataset

def create_model(vocabulary_size, sequence_length, embedding_dim, num_classes):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=vocabulary_size, output_dim=embedding_dim),
        # tf.keras.layers.LSTM(64),  # You can also use GRU here
        # # tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(num_classes)
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def make(num_sequences: int, sequence_length: int, embedding_dim: int):
    input_shape = (sequence_length, embedding_dim)
    model = create_model(dataset.vocabulary_size, dataset.sequence_length, dataset.embedding_dim, 2)
    model.summary()
    return model
