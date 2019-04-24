from nltk import word_tokenize
from nltk import Text
from nltk import FreqDist
from nltk import bigrams
from nltk import ngrams

tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)
from nltk.book import *
words = tokens
fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
print("words how many times?",fourgramsDist[("father", "smelt", "of", "elderberries")])

for fourgram in fourgrams:
    if fourgram[0] == "coconut":
        print(fourgram)