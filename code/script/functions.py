import re
import numpy as np 
import pandas as pd 
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import one_hot

def initial_check(path, delimiter=None, index_col=None):
    df = pd.read_csv(path, index_col=index_col, delimiter=delimiter)
    print(f'Duplicated values: {df.duplicated().sum()}')
    print(df.info())
    return df

#Regex is taken from https://www.kaggle.com/ankitkumarsaini/distilbert 
def text_cleaning(text):
    forbidden_words = set(stopwords.words('english'))
    if text:
        text = ' '.join(text.split('.'))
        text = re.sub('\/',' ',text)
        text = re.sub(r'\\',' ',text)
        text = re.sub(r'((http)\S+)','',text)
        text = re.sub(r'\s+', ' ', re.sub('[^A-Za-z]', ' ', text.strip().lower())).strip()
        text = re.sub(r'\W+', ' ', text.strip().lower()).strip()
        text = [word for word in text.split() if word not in forbidden_words]
    return " ".join(text)

def text_processing(dataframe):
    '''Returns a dataframe where the cleaning function (text_cleaning) is applied to the Pharse column. Followed by the removal of blank and duplicated rows'''
    df = dataframe.copy()
    #Cleans the dataframe using the text_cleaning function above
    df['Phrase'] = df['Phrase'].map(text_cleaning)
    #Removes rows that have blank in Phrase
    df = df.loc[df['Phrase'].map(lambda x: len(x.split())) > 0]
    #Remove duplicates
    df = df.drop_duplicates(subset=['Phrase'])
    return df 

def unique_word_count(df):
    '''Returns the count of unique words'''
    a = df.copy()
    phrases = [] 
    for phrase in a['Phrase'].tolist():
        for word in phrase.split():
            phrases.append(word)
    return len(set(phrases))

def encode_and_pad(df, vocab_size, max_len = 500):
    a = df.copy()
    vocab_size = vocab_size
    max_len = max_len
    a['encoding'] = a['Phrase'].map(lambda x: one_hot(x, vocab_size)) 
    return sequence.pad_sequences(a['encoding'], max_len, padding='post', truncating='post'), a