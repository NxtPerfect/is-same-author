# Data
- [x] find dataset with text and author listed
preferably, texts from the same person, the longer the better
    - [x] scrape text from book?
        this would ensure same author
        and we could test it like i want it to
        - [x] insert into csv with author, text
            - [x] write script to organize it into 50 words
            with ",author" at the end
            if line is too short
            add it to list and then if next line makes it > 50, split at next . ! ?
            and write to file at first line from stack, then remove the ones we used
            to make it longer
        - [x] add data from different authors

# Training
- [x] load text, and author as training data

# Model
- [x] find appropriate activation function
    linear regression
- [x] find model architecture
- [/] output proper shape

# Gui
- [ ] text field to paste dataset
    - [ ] and load data from csv
- [ ] text field to paste test data
- [ ] label to show if same author
- [ ] show percentage of confidence
- [ ] debug info, change epochs, etc
