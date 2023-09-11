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