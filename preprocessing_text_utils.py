import ast
import re
import nltk
import pandas as pd
import emoji

# Function to load the contraction file from text file
def load_contraction_dicts():
    # read the contraction dict from text file
    with open('./Data/contraction.txt') as f:
        contractions = f.read()
    #convert the str back to dict type with ast method
    contraction_dicts = ast.literal_eval(contractions)
    return contraction_dicts
    
# Function for expanding contractions
def expand_contractions(text, contractions_dict):
    # Regular expression for finding contractions
    contractions_re=re.compile('(%s)' % '|'.join(contractions_dict.keys()))
    def replace(match):
        return contractions_dict[match.group(0)]
    return contractions_re.sub(replace, text)

# Function to clean text from punctuations
def clean_text(text: str):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('[^\w\s]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    return text


def remove_emoji(text):
    text = emoji.replace_emoji(text, replace="")
    return text


# Function to remove stop words
def stop_words_removal(text : list):
    '''
    Remove stop words i.e most common words found in a language, but there is no single universal list of stop words.
    '''
    stopwords = nltk.corpus.stopwords.words('english')
    text = [word for word in text if word not in stopwords]
    return text

# Function to stem the text
def stemming(text):
    '''
    Technique to extract the base form of words by removing prefixes such as (-ing, -ly, ...)
    example  --> 'beautiful' -> 'beauti', 'caring' -> 'car'
    '''
    ps = nltk.stem.porter.PorterStemmer()
    stem_text = [ps.stem(word) for word in text]

    return stem_text

# Function to lemmatize the text
def lemmatize(text: list):
    '''
    Technique to extract the meaningful base form of a word
    example  --> 'beautiful' -> 'beauty', 'caring' -> 'care'
    '''
    lemma = nltk.stem.wordnet.WordNetLemmatizer()
    lemma_text = [lemma.lemmatize(word) for word in text]

    return lemma_text

# Function to process the text
def process_text(text, do_stem= False, do_lemmatization = False):
    text = text.lower()
    text = expand_contractions(text, load_contraction_dicts())
    text = clean_text(text)
    text = remove_emoji(text)
    text = text.split()
    text = stop_words_removal(text)
    if do_stem == True:
        text = stemming(text)
    elif do_lemmatization == True:
        text = lemmatize(text)
    
    ## back to string from list
    text = " ".join(text)
    return text

def length_analysis(new_df: pd.DataFrame, column : str):
    df = new_df.copy()
    df['word_count'] = df[column].apply(lambda x: len(str(x).split(" ")))
    df['char_count'] = df[column].apply(lambda x: sum(len(word) for word in str(x).split(" ")))
    df['sentence_count'] = df[column].apply(lambda x: len(str(x).split(".")))
    df['avg_word_length'] = df['char_count'] / df['word_count']
    df['avg_sentence_lenght'] = df['word_count'] / df['sentence_count']

    return df

