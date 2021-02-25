# Sentiment Analysis on Movie Reviews

The repo is inspired by the kaggle competion to classify the sentiment of sentences from the a Rotten Tomatoes dataset. The link to the [competition](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews). 

## Project File
### Main Directory/
- README.md: Project summary document (this file)
- **code/**
    - **script/**
        - functions.py: Python script containing function codes for cleaning data
    - 01_data_cleaning_modeling.ipynb: Notebook containg data cleaning and the baseline model
    - 02_EDA.ipynb: Notebook containing EDA
    - 03_random_forrest: Notebook containing notes and modeling of random forrest
- **data/**
    - test.tsv: Raw testing data
    - train.tsv: Raw training data
    - clean_test.csv: Clean test data
    - clean_train.cssv: Clean train data
- **img/**: Directory containing image files for figures and charts
- **models/**: Directory containing pickled models 

## Data Set

The dataset is a corpus of movie reviews used for sentiment analysis. The data was orginally collected by [Pand and Lee][1].

### Data Directory: 
|Column Name|Data Type|Description|
|-----------|---------|-----------|
|PhraseId |int|Unique key identifers for each phrases|
|SentenceId|int| Key identifiers for each setences|
|Phrase|object/string|Movie reviews broken down to phrases using Stanford parser|
|Sentiment|int|Sentiment ratings ranging from 0-4 (0 - negative, 1 - somewhat negative, 2 - neutral, 3 - somewhat positive, 4 - positive)|

## Refernces

[1]: Pang and L. Lee. 2005. Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales. In ACL, pages 115–124



