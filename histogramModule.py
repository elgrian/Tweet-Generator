import re
import sys
import string
import random
# file = str(sys.argv[1])
# text = str(sys.argv[1])
# def read_file(file):
#     document_text = open(file, 'r')
#     text_string = document_text.read().lower()
#     document_text.close()
#     return text_string
#----------LIST_OF_LISTS---------------
def list_of_lists(text):
    document_text = open(text, 'r')
    text_string = document_text.read().lower()
    document_text.close()
    match_pattern = re.findall(r'\b[a-z]{1, 15}\b', text_string)
    # match_pattern.sort() #Maybe use this
    list_array = []
    count = 0
    index = None
    for word in match_pattern:
        if word == index:
            count += 1
        else:
            list_array.append([index, count])
            index = word
            count = 1
    else:
        
        list_array.append([index, count])
        list_array.pop(0)
    return str(list_array)
#------END OF LIST_OF_LISTS-------------        

#----------LIST_OF_TUPLES---------------


def list_of_tuples(text):
    frequency = {}
    first_list = []
    second_list = []
    document_text = open(text, 'r')
    text_string = document_text.read().lower()
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
    # 
    # unique_count = 0
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
        first_list.append(word)
        # if int(frequency[word]) == 1:
        #     unique_count += 1
    for word in match_pattern:
        second_list.append(int(frequency[word]))

    zipped = zip(first_list, second_list)
    # 
    # print(list(set(zipped)))
    
    denominator = int(len(text_string))
    n = random.randrange(0, denominator)
    for word in first_list:
        for i in second_list:
            n = random.randrange(0, denominator)
            if i > n:
                print(word)
    # print("Unique words: " + str(unique_count))
    # print(len(match_pattern))

#----------END OF LIST_OF_TUPLES---------
    
    
#----------DICTIONARY FUNCTION-----------
def dictionary_histogram(text):
    document_text = open(text, 'r')
    text_string = document_text.read().lower()
    match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
    dict_histo = {}
    for word in match_pattern:
        if word not in dict_histo:
            dict_histo[word] = 1
        else:
            dict_histo[word] += 1
    
    def unique_word_dict(dict_histo):
        ''' Takes the histogram and returns the amount of unique words withi it.'''
        return len(dict_histo.keys())
    def frequency(dict_histo, word):
        '''takes in the histogram and a word, then returns a value of the word if the
        key exists within the dictionary, else return 0'''
        if word in histogram:
            return str(dict_histo[word])
        else:
            return str(0)
    
    # print(str(dict_histo))
    
    def dict_probability(dict_histo):
        # random_sum = random.randint(0, sum(dict_histo.values()))
        dict_sum = random.randrange(dict_histo)
        accum = 0
        for key, value in dict_histo.items():
            accum += value
            if accumulator >= dict_sum:
                return key
            else:
                continue
    print(str(list(dict_probability)))
        # print(list(dict_histo(text)))
        
#------------End of Dictionary-----------------

if __name__ == '__main__':
    text = 'example.txt'
    dictionary_histogram(text)
    # dictionary_histogram(text)
    




    