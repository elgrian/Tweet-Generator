import re
import sys
import string

def read_file(file):
    document_text = open(file, 'r')
    text_string = document_text.read().lower()
    # match_pattern = re.findall(r'\b[a-z]{1, 15}\b', text_string)   ### Think I should move this to the actual list function maybe??? 
    ### I originally had it return match_pattern and then I used match_pattern in my list functions i.e list_of_lists(match_pattern)
    document_text.close()
    return text_string
#----------LIST_OF_LISTS---------------
def list_of_lists(text_string):
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
def list_of_tuples(text_string):
    match_pattern = re.findall(r'\b[a-z]{1, 15}\b', text_string)
    frequency = {}
    first_list = []
    second_list = []
    unique_count = 0
    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
        first_list.append(word)
        if int(frequency[word]) == 1:
            unique_count += 1
            
    for word in match_pattern:
        second_list.append(int(frequency[word]))    
        
    zipped = zip(first_list, second_list)
    # return list(set((zipped)))
    return str(list(set(zipped)))
    # return str("There are " + str(unique_count) + " words in this file")
#----------END OF LIST_OF_TUPLES---------
    
    
#----------DICTIONARY FUNCTION-----------
def dictionary_histogram(text_string):
    dict_histo = {}
    for word in match_pattern:
        if word not in dict_histo:
            dict_histo[word] = 1
        else:
            dict_histo[word] += 1
    return str(dict_histo)
    
    def unique_word_dict(histogram):
        ''' Takes the histogram and returns the amount of unique words withi it.'''
        return len(histogram.keys())
        
    def frequency(histogram, word):
        '''takes in the histogram and a word, then returns a value of the word if the
        key exists within the dictionary, else return 0'''
        if word in histogram:
            return str(histogram[word])
        else:
            return str(0)
#------------End of Dictionary-----------------
# 
# def unique_word(histogram):
#     ''' Takes the histogram and returns the amount of unique words withi it.'''
#     return len(histogram)
# 
# def frequency(word, histogram):
#     '''takes a histogram and a word, then returns the value of the word.'''
#     return histogram[word]

# read_file(file)
# list_of_tuples(read_file(file))
if __name__ == '__main__':
    file = str(sys.argv[1])
    # print(list_of_lists(read_file(file)))


    