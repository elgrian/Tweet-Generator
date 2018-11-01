import timeit, sys
###--------------OPEN FILE-------------------------------------
def get_text_file(file):
    '''Opens a file, puts the words into an array, then closes
     the file and returns the array of strings and then makes all the words lowercase.'''
    f = open(file, "r")
    array = f.read().split().lower()
    f.close()
    return array
    
#--------------STRIP AWAY PUNCTUACTION--------------------------
def strip_punc(array):
    '''opens the array of strings, cycles through each word, and then
    creates a copy of the word without punctuation then returns the array.'''
    punctuation = ["@" , "#" , "$" , ":", ";", "_", "*" , "}" , "[" , "{" , "]" , "," , ".", "!" , "?"]
    for i, word in enumerate(array):
        fixed_word = ""
        for char in word:
            if char not in punctuation:
                fixed_word += char
        array[i] = fixed_word
    return array
    
#------------Dictionary HistogramLists -------------------------
def countWords(array):
    '''Takes an array of words and sorts them into a diction with the word and the 
    frequency of the word as a key value.'''
    histo_dict = {}
    for word in array:
        if word not in histo_dict:
            histo_dict[word] = 1
        else:
            histo_dict[word] += 1
    return histo_dict
    
def unique_words(histogram):
    '''takes a histogram and returns the amount of words in it that are unique.'''
    return len(histogram.keys())
       
    
def frequency(histogram, word):
    '''takes in the histogram and a word, then returns a value of the word if the
    key exists within the dictionary, else return 0'''
    if word in histogram:
        return histogram[word]
    else:
        return str(0)
#--------------End of Dictionary Histogram-----------------------    
    
    
#----------List of Lists Histogram-------------------------------
def count_words_array(array):
    '''takes an array of words (string) and sorts them alphabetically,
    cycles through the array and counts the entries in that order,
    appending an array of the word and the word's frequency to the array'''
    list_array = []
    count = 0
    index = None
    for word in array:
        if word == index:
            count += 1
        else:
            list_array.append([index, count])
            list_array.pop(0)
        return list_array
        