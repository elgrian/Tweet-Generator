import random
import re

histogram_dictionary = {}
#Takes in text and returns a histogram(dictionary) of word frequency that shows word frequency
def histogram(text):
    for word in text:
        if word in histogram_dictionary:
            histogram_dictionary[word] += 1
        else:
            histogram_dictionary[word] = 1
            
    return histogram_dictionary

