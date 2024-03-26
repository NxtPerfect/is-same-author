import pandas as pd
import numpy as np
import tensorflow as tf

np.set_printoptions(precision=3, suppress=True)

sampleData = ["This is a sample data", "And here's another"]
labels = [0, 1]

def loadDataFromCsv(path: str):
    sampleData = pd.read_csv(path, names=["Text", "Author"])
    sampleData.head()
    return sampleData

def tokenizeAndVectorize():
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(sampleData)
    sequences = tokenizer.texts_to_sequences(sampleData)

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

if __name__ == "__main__":
    sampleData = loadDataFromCsv("data.bak/sample1.csv")
    sampleDataFeatures = sampleData.copy()
    sampleDataLabels = sampleDataFeatures.pop('Text')
    
    sampleDataFeatures = np.array(sampleDataFeatures)
    print("Aha see", sampleDataFeatures)

    sequences = tokenizeAndVectorize()
    sequences = uniformSequences(sequences)
    labels = labelsToCategorical(labels)
    dataset = createDataset(sequences, labels)

    print(dataset)
