from flask import request, jsonify
from nltk.stem.wordnet import WordNetLemmatizer
# from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

def job():
  #if want to stem or lemm
  doLemm = False
  resultQuery = ''
  if request.args.get('lem') == 1:
    doLemm = True

  if request.args.get('query'):
    query = request.args.get('query')
    # query = request.json.get('query')
    query = query.split()

    if request.args.get('stopwords'):
      stop_words = set(stopwords.words('english'))
      stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) # remove it if you need punctuation 
      query = [word for word in query if word not in stop_words]

    if doLemm == True:
      resultQuery = lemm_words(query)
    else:
      resultQuery = stemm_words(query)

    return jsonify({'data': resultQuery})
  else:
    return jsonify({'status': False, 'message': 'Please provide valid input'})

# Use Lemmatizer
def lemm_words(query):
  lmtzr = WordNetLemmatizer()
  query = [lmtzr.lemmatize(word) for word in query]
  return query

# Use Stemmer
def stemm_words(query):
  # stemmer = PorterStemmer()
  stemmer = SnowballStemmer("english")
  query = [stemmer.stem(word) for word in query]
  # query = ' '.join(query)
  return query