import src.model
import src.dataset

def train():
    dataset = src.dataset.create("data.bak/output2.csv")
    train_dataset, val_dataset = src.dataset.preprocess_data(dataset)
    model = src.model.make()

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    history = model.fit(train_dataset, validation_data=val_dataset, epochs=10, batch_size=32)

    # Evaluate the model
    loss, accuracy = model.evaluate(val_dataset)

    print("Validation Loss:", loss)
    print("Validation Accuracy:", accuracy)

    # Save the model
    model.save("model.h5")
