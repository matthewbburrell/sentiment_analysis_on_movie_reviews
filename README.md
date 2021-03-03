# Sentiment Analysis on Movie Reviews

The repo is inspired by the kaggle competion to classify the sentiment of sentences from the a Rotten Tomatoes dataset. The link to the [competition](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews). 

## Project File
### Main Directory/
- README.md: Project summary document (this file)
- **code/**
    - **script/**
        - functions.py: Python script containing function codes for cleaning data
    - 01_data_cleaning.ipynb: Notebook containing explanation for the cleaning process
    - 02_EDA.ipynb: Notebook containing EDA
    - 03_data_modeling.ipynb:
- **data/**
    - test.tsv: Raw testing data
    - train.tsv: Raw training data
    - clean_test.csv: Clean test data
    - clean_train.cssv: Clean train data
- **img/**: Directory containing image files for figures and charts
- **models/**: Directory containing pickled models 

## Data Description

The dataset is comprised of tab-separated files with phrases from the Rotten Tomatoes dataset. The train/test split has been preserved for the purposes of benchmarking, but the sentences have been shuffled from their original order. Each Sentence has been parsed into many phrases by the Stanford parser. Each phrase has a PhraseId. Each sentence has a SentenceId. Phrases that are repeated (such as short/common words) are only included once in the data.

- train.tsv contains the phrases and their associated sentiment labels. We have additionally provided a SentenceId so that you can track which phrases belong to a single sentence.
- test.tsv contains just phrases. You must assign a sentiment label to each phrase.

The sentiment labels are:

0 - negative\
1 - somewhat negative\
2 - neutral\
3 - somewhat positive\
4 - positive

### Data Directory: 
|Column Name|Data Type|Description|
|-----------|---------|-----------|
|PhraseId |int|Unique key identifers for each phrases|
|SentenceId|int| Key identifiers for each setences|
|Phrase|object/string|Movie reviews broken down to phrases using Stanford parser|
|Sentiment|int|Sentiment ratings ranging from 0-4 (0 - negative, 1 - somewhat negative, 2 - neutral, 3 - somewhat positive, 4 - positive)|


## Refernces

[1]: Pang and L. Lee. 2005. Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales. In ACL, pages 115–124



