# Assignment no:-01
# Name:-Prajakta Sambhaji KOlse
# Subject:-NLP
# Roll no:-34 , Batch:-B2
# Title:- Text Pre-Processing using NLP operations:perform Tokenization,StopWords,Lemmatization,Part-of-speech Tagging.

# Title:-Tokenization
# Import Library
import spacy

nlp = spacy.load("en_core_web_sm")
about_text = (
    "Hello, I am Prajakta Kolse from Rahuri."
    "Pursuing Btech degree in Information Technology"
    " from Sanjivani Collge Of Engineering , Kopargaon"
    " Natural Language Processing."
)
about_doc = nlp(about_text)

#Tokenization
for token in about_doc:
    print (token, token.idx)

#Title : Stop words
import spacy
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
# Stop Word
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)



custom_about_text = (
    "Hello, I am Prajakta Kolse from Rahuri."
    "Pursuing Btech degree in Information Technology"
    " from Sanjivani Collge Of Engineering , Kopargaon"
    " Natural Language Processing."
)
nlp = spacy.load("en_core_web_sm")
about_doc = nlp(custom_about_text)
#List Of STop words
print([token for token in about_doc if not token.is_stop])


#Title: Lemmitization
#import Library
import spacy
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
  "Hello, I am Prajakta Kolse from Rahuri."
    "Pursuing Btech degree in Information Technology"
    " from Sanjivani Collge Of Engineering , Kopargaon"
    " Natural Language Processing."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


#Title :Part of Speech tagging

# import library

import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "Hello, I am Prajakta Kolse from Rahuri."
    "Pursuing Btech degree in Information Technology"
    " from Sanjivani Collge Of Engineering , Kopargaon"
    " Natural Language Processing."
)
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )