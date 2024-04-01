import pandas as pd
import numpy as np
import tensorflow as tf

np.set_printoptions(precision=3, suppress=True)

def loadDataFromCsv(path: str):
    sampleData = pd.read_csv(path, names=["Text", "Author"])
    sampleData.head()
    return sampleData

def tokenizeAndVectorize(data):
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(data)
    sequences = tokenizer.texts_to_sequences(data)

    return sequences

def uniformSequences(text: str):
    max_length = max(len(seq) for seq in text)
    sequences = tf.keras.preprocessing.sequence.pad_sequences(text, maxlen=max_length)

    return sequences

def labelsToCategorical(labels: list):
    num_classes = len(set(labels))
    labels = tf.keras.utils.to_categorical(labels, num_classes=num_classes)

    return labels

def createDataset(sequences: str, labels: list):
    dataset = tf.data.Dataset.from_tensor_slices((sequences, labels))

    return dataset

def preprocess_data(dataset):
    # Split the dataset into features (X) and labels (y)
    X = dataset['Text'].values
    y = dataset['Author'].values

    # Tokenize the text data
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(X)
    X = tokenizer.texts_to_sequences(X)

    # Pad sequences to ensure they have the same length
    max_length = 50  # maximum sequence length
    X = tf.keras.preprocessing.sequence.pad_sequences(X, maxlen=max_length)

    # Convert labels to categorical format (if needed)
    y = tf.keras.utils.to_categorical(y)

    # Split the data into training and validation sets
    # You may need to adjust the split ratio based on your dataset size
    validation_split = 0.2
    num_validation_samples = int(validation_split * len(X))

    train_X = X[:-num_validation_samples]
    train_y = y[:-num_validation_samples]

    val_X = X[-num_validation_samples:]
    val_y = y[-num_validation_samples:]

    # Create TensorFlow Datasets for training and validation
    train_dataset = tf.data.Dataset.from_tensor_slices((train_X, train_y))
    val_dataset = tf.data.Dataset.from_tensor_slices((val_X, val_y))

    return train_dataset, val_dataset

def create(source_path: str):
    labels = [0, 1]
    sampleData = loadDataFromCsv(source_path)
    sampleDataFeatures = sampleData.copy()
    # sampleDataLabels = sampleDataFeatures.pop('Text')
    
    sampleDataFeatures = np.array(sampleDataFeatures)
    # print("Aha see", sampleDataFeatures)

    sequences = tokenizeAndVectorize(sampleData)
    sequences = uniformSequences(sequences)
    labels = labelsToCategorical(labels)
    dataset = createDataset(sequences, labels)

    return dataset
