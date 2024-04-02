import model
import dataset
import tensorflow as tf

def train():
    data = dataset.create("data.bak/output2.csv")
    train_dataset, val_dataset = dataset.preprocess_data("data.bak/output2.csv")

    m = model.make(dataset.num_sequences, dataset.sequence_length, dataset.embedding_dim)

    # Compile and train the model
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    history = m.fit(train_dataset, validation_data=val_dataset, epochs=10, batch_size=32)

    # Evaluate the model
    loss, accuracy = m.evaluate(val_dataset)
    print("Validation Loss:", loss)
    print("Validation Accuracy:", accuracy)

    # Save the model
    m.save("model.h5")

if __name__ == "__main__":
    train()
