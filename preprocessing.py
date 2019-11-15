import pickle as pk
import sys
import warnings
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
import re



def lower_case(sentences):
    return [sentence.lower() for sentence in sentences]

def keep(sentences,labels,ratio):
    data_size = int(len(sentences) * ratio)
    sentences = self.sentences[:data_size]
    labels    = self.labels[:data_size]
    return sentences,labels

def split_data(sentences,labels):
    X_train, X_val, y_train, y_val = train_test_split(sentences, labels, train_size=0.8)
    return X_train, X_val, y_train, y_val


def cleanHtml(sentence):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', str(sentence))
    return cleantext


def cleanPunc(sentence): #function to clean the word of any punctuation or special characters
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    cleaned = cleaned.strip()
    cleaned = cleaned.replace("\n"," ")
    return cleaned


def keepAlpha(sentence):
    alpha_sent = ""
    for word in sentence.split():
        alpha_word = re.sub('[^a-z A-Z]+', ' ', word)
        alpha_sent += alpha_word
        alpha_sent += " "
    alpha_sent = alpha_sent.strip()
    return alpha_sent



stop_words = set(stopwords.words('english'))
re_stop_words = re.compile(r"\b(" + "|".join(stop_words) + ")\\W", re.I)
def removeStopWords(sentence):
    global re_stop_words
    return re_stop_words.sub(" ", sentence)



stemmer = SnowballStemmer("english")
def stemming(sentence):
    stemSentence = ""
    for word in sentence.split():
        stem = stemmer.stem(word)
        stemSentence += stem
        stemSentence += " "
    stemSentence = stemSentence.strip()
    return stemSentence


def tf_idf(train_sentences,test_sentences):
    vectorizer = TfidfVectorizer(strip_accents='unicode', analyzer='word', ngram_range=(1,3), norm='l2')
    vectorizer.fit(train_sentences)
    vectorizer.fit(test_sentences)
    x_train = vectorizer.transform(train_text)
    x_test = vectorizer.transform(test_text)
    
    return x_train,x_test


#demo data
def get_keras_data():
    
    with open('./better/r_steamed_st.pkl','rb') as f:
        sentences = pk.load(f)
    with open('./better/r_steamed_lb.pkl','rb') as f:
        labels = pk.load(f)
        
    return lower_case(sentences), labels

def get_retu_data(keep_ratio):
    
    with open('reuters_sentences_st.pkl','rb') as f:
        sentences = pk.load(f)
    
    with open('all_raw_labels_keras.pkl','rb') as f:
        labels = pk.load(f)

    with open('label_order_keras.pkl','rb') as f:
        columns = pk.load(f)

    with open('label_encoding_keras.pkl','rb') as f:
        label_embedding = pk.load(f)

    with open('one_hot_encoding_keras.pkl','rb') as f:
        one_hot = pk.load(f)

    with open('adj_matrix_keras.pkl','rb') as f:
        adj_matrix = pk.load(f)
        
    
        
    if keep_ratio:
        sentences, labels = keep(sentences,labels,keep_ratio)
        
        
    return lower_case(sentences),labels,columns,label_embedding,one_hot,adj_matrix