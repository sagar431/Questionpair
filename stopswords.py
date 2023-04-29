import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
import pickle

STOP_WORDS = set(stopwords.words('english'))

with open('stopwords.pkl', 'wb') as f:
    pickle.dump(STOP_WORDS, f)
