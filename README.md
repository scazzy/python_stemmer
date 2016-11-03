# python_stemmer
RESTFUL api in python to stemming and lemmatizing input query.

## Features
- Uses Flask micro framework for routing and other base stuff
- Uses NLTK corpus for lemmatizing with WordNet
- Uses SnowballStemmer for stemming

## Options [GET]
query (string)
lem = 1/0 (default 0, if to lemmatizes. else will stem)
stopwords (if to remove stopwords, from NLTK corpus)


---- This is a test project to try create a restful api to get sanitized keywords to be used in the original application