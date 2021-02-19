import re
import pandas as pd 
from nltk.corpus import stopwords

#See https://www.kaggle.com/ankitkumarsaini/distilbert for function description
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
    df = dataframe.copy()
    #Cleans the dataframe using the text_cleaning function above
    df['Phrase'] = df['Phrase'].map(text_cleaning)
    #Removes rows that have blank in Phrase
    df = df.loc[df['Phrase'].map(lambda x: len(x.split())) > 0]
    #Remove duplicates
    df = df.drop_duplicates(subset=['Phrase'])
    return df 