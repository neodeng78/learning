from nltk import word_tokenize
from nltk import Text
import nltk
from nltk import FreqDist
from nltk import bigrams

tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)
from nltk.book import *
words = tokens
print(words)
print(len(text6)/len(words))


fdist = FreqDist(text6)
print(fdist.most_common(10))


bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
print("*"*50)

print("bigramsDist 'Sir' 'Robin': ",bigramsDist[("Sir", "Robin")])