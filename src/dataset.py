import pandas as pd
import numpy as np
import tensorflow as tf

np.set_printoptions(precision=3, suppress=True)
num_sequences = 0
num_classes = 0
sequence_length = 0
embedding_dim = 0
vocabulary_size = 0

def loadDataFromCsv(path: str):
    sampleData = pd.read_csv(path, names=["Text", "Author"], delimiter=';')
    # Convert 'Author' column to numeric labels
    sampleData['Author'] = pd.Categorical(sampleData['Author'])
    sampleData['Author'] = sampleData['Author'].cat.codes
    sampleData.head()
    print(sampleData)
    return sampleData

def split_text_into_sentences(text):
    # Split text into sentences using punctuation marks as delimiters
    sentences = [sentence.strip() for sentence in re.split(r'(?<=[.!?])\s+', text)]
    return sentences

def tokenizeAndVectorize(data):
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(data)
    vocabulary_size = len(tokenizer.word_index) + 1
    sequences = tokenizer.texts_to_sequences(data)

    return sequences, tokenizer

def uniformSequences(text: str):
    max_length = max(len(seq) for seq in text)
    sequences = tf.keras.preprocessing.sequence.pad_sequences(text, maxlen=max_length, padding='post', truncating='post')

    return sequences

def labelsToCategorical(labels: list):
    num_classes = len(set(labels))
    labels = tf.keras.utils.to_categorical(labels, num_classes=num_classes)

    return labels

def createDataset(sequences: str, labels: list):
    dataset = tf.data.Dataset.from_tensor_slices((sequences, labels))

    return dataset

# def preprocess_data(dataset):
#     # dataset = tf.data.Dataset.from_tensor_slices(dataset)
#     # Define a parsing function
#     def parse_fn(text, author):
#         return text, author
#
#     # Apply the parsing function to each element of the dataset
#     dataset = dataset.map(parse_fn)
#
#     # Split the dataset into training and validation sets
#     validation_split = 0.2
#     num_validation_samples = int(validation_split * len(dataset))
#
#     train_dataset = dataset.skip(num_validation_samples)
#     val_dataset = dataset.take(num_validation_samples)
#
#     return train_dataset, val_dataset

def preprocess_data(dataset_path: str):
    # Load data from CSV
    data = loadDataFromCsv(dataset_path)

    # Tokenize and vectorize the text data
    sequences, tokenizer = tokenizeAndVectorize(data['Text'])
    sequences = uniformSequences(sequences)

    # Convert labels to categorical format
    labels = tf.keras.utils.to_categorical(data['Author'], num_classes=len(set(data['Author'])))

    # Split data into training and validation sets
    validation_split = 0.2
    num_validation_samples = int(validation_split * len(sequences))

    train_sequences = sequences[:-num_validation_samples]
    train_labels = labels[:-num_validation_samples]

    val_sequences = sequences[-num_validation_samples:]
    val_labels = labels[-num_validation_samples:]

    # Create TensorFlow Datasets for training and validation
    train_dataset = tf.data.Dataset.from_tensor_slices((train_sequences, train_labels))
    val_dataset = tf.data.Dataset.from_tensor_slices((val_sequences, val_labels))

    return train_dataset, val_dataset

def create(source_path: str):
    labels = [0, 1]
    sampleData = loadDataFromCsv(source_path)
    sampleDataFeatures = sampleData.copy()
    sampleDataLabels = sampleDataFeatures.pop('Text')

    print("Shape of data:", sampleData.shape)
    
    sampleDataFeatures = np.array(sampleDataFeatures)
    # print("Aha see", sampleDataFeatures)

    sequences, tokenizer = tokenizeAndVectorize(sampleData)
    sequences = uniformSequences(sequences)
    labels = labelsToCategorical(labels)

     # Assign values to global variables
    num_sequences = len(sequences)
    sequence_length = sequences.shape[1]
    embedding_dim = len(tokenizer.word_index) + 1  # Add 1 for padding token
    dataset = createDataset(sequences, labels)

    return dataset
