import random # to generate random numbers
import re # for regular expressions

def histogramTuple(url):
    file = open(url, 'r')

    content = file.read().lower()
    list_of_words = re.split('\W+', content) # replaces not (^) word characters with an empty string
    file.close()

    unique_list_of_words = [] # create empty list
    word_counter = [] # empty list that will have count per word at same index as unique_list_of_words

    for word in list_of_words:
        if word not in unique_list_of_words:
            # add to list
            unique_list_of_words.append(word)
            word_counter.append(1)
        else:
            # word is already in list, increment word_counter at same index as word
            word_counter[unique_list_of_words.index(word)] += 1 # increment word_counter for the same index

    histogram = []
    i = 0
    for word in unique_list_of_words:
        histogram.append((unique_list_of_words[i], word_counter[i]))
        i += 1

    return histogram # return a data structure that stores ea. unique word & of times the word appears

def unique_words(histogram):
    return len(histogram) # return the total count of unique words in the histogram.


def frequency(word, histogram):
    return int(histogram[word]) # returns the number of times that word appea

if __name__ == '__main__':

    histogram = histogramTuple('frankenstein.txt')
    print(histogram)
    

###### Instead of doing that dumb shit read function, make it read once within the damn ass function bitch
