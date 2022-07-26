import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def generate_ngrams(text, ngram_from = 1, ngram_to = 1, n = None, max_features = 200000):
    vec = CountVectorizer(ngram_range= (ngram_from, ngram_to), max_features=max_features, stop_words= 'english').fit(text)
    bow = vec.transform(text)
    sum_words = bow.sum(axis = 0)
    words_freq = [(word, sum_words[0, i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x : x[1], reverse = True)
    return words_freq[:n]

def ngrams_df(ngrams, columns = ['Word', 'Frequency']):
    df = pd.DataFrame(ngrams, columns=columns)
    return df

