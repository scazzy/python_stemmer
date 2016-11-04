# python_stemmer
RESTFUL api in python to stemming and lemmatizing input query.

## Features
- Uses Flask micro framework for routing and other base stuff
- Uses NLTK corpus for lemmatizing with WordNet
- Uses SnowballStemmer for stemming

## Options [GET]
* query (string)
* lem = 1/0 (default: 0, if to lemmatizes. else will stem)
* stopwords = 1/0 (default: 0, if to remove stopwords, from NLTK corpus)


## Requirements
* Install Flask using `pip install Flask` or follow http://flask.pocoo.org/docs/0.11/installation/
* Install NLTK. Follow http://www.nltk.org/install.html
* (optional) Install/Download NLTK corpus, if using lemmatizer

--
This is a test project to try create a restful api to get sanitized keywords to be used in the original application
