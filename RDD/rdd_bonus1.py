# open all the words of the cleaned RDD from RDD basic part


Num_topics = input("Please input number of topics you want: ")
F = input("Please put the file path: ")

# F = "bagOfWords.txt/part-00000"
with open(F) as f:
    mylist = list(f)
    

# Run in python console
import nltk
nltk.download('stopwords')


import spacy
spacy.load('en')
from spacy.lang.en import English
parser = English()
def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens
    

import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
from nltk.stem.wordnet import WordNetLemmatizer
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)
    

nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))

def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens
    
import random
text_data = []
F = "bagOfWords.txt/part-00000"
with open(F) as f:
    for line in f:
        tokens = prepare_text_for_lda(line)
        if random.random() > .99:
            text_data.append(tokens)

print(text_data[1:200])

# remove empty lists
text_data = [x for x in text_data if x != []]
print(text_data[1:300])

## LDA With Gensim
# we are creating a dictionary from the data, then convert to 
# bag-of-words corpus
#and save the dictionary and corpus for future use.
from gensim import corpora
dictionary = corpora.Dictionary(text_data)
corpus = [dictionary.doc2bow(text) for text in text_data]
import pickle
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')

# We are asking LDA to find 10 topics in the data:
import gensim
NUM_TOPICS = Num_topics
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
ldamodel.save('model5.gensim')
topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)
    # index is the topic number
    
    

# The package extracts information from a fitted LDA topic model
# to inform an interactive web-based visualization.
dictionary = gensim.corpora.Dictionary.load('dictionary.gensim')
corpus = pickle.load(open('corpus.pkl', 'rb'))

# load the model
lda = gensim.models.ldamodel.LdaModel.load('model5.gensim')
import pyLDAvis.gensim
# lda_display = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=False)
# pyLDAvis.display(lda_display)

p = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.save_html(p, 'lda.html')

#we can see certain topics are clustered together,
#this indicates the similarity between topics.


# take note i will now write this as a script to tell user to choose 
# num of topics they want
# input the txt document of choice
