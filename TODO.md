# Data
- [/] find dataset with text and author listed
preferably, texts from the same person, the longer the better
    - [/] scrape text from book?
        this would ensure same author
        and we could test it like i want it to
        - [/] insert into csv with author, text
            - [ ] write script to organize it into 50 words
            with ",author" at the end
            if line is too short
            add it to list and then if next line makes it > 50, split at next . ! ?
            and write to file at first line from stack, then remove the ones we used
            to make it longer
        - [ ] add data from different authors

# Training
- [ ] load text, and author as training data

# Model
- [ ] find appropriate activation function
- [ ] find model architecture

# Gui
- [ ] text field to paste dataset
    - [ ] and load data from csv
- [ ] text field to paste test data
- [ ] label to show if same author
- [ ] show percentage of confidence
- [ ] debug info, change epochs, etc
