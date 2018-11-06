import random

histogram_dictionary = {}
#Takes in text and returns a histogram(dictionary) of word frequency that shows word frequency
def histogram(text):
    for word in text:
        if word in histogram_dictionary:
            histogram_dictionary[word] += 1
        else:
            histogram_dictionary[word] = 1
            
    return histogram_dictionary


def random_word(histogram_dictionary):
    '''Takes a Dictionary as a histogram and returns a random key from it'''
    #Creates a running total value
    accum = 0
    #Gets a random number between 0 and the total sum of all frequencies
    sum_dictionary = sum(histogram_dictionary.values())
    random_sum = random.randint(1, sum_dictionary) # Either [1 - sum] or [0, sum - 1] otherwise it repeats inappropraitely
    # ".items()" allows the dictionary to be iterated over
    for key, value in histogram_dictionary.items():
        accum += value
        if accum > random_sum:
            return key
        else:
            continue
            
def dictionary_test(histogram_dictionary):
    test_dictionary = {}
    for _ in range(0, 10000):
        selected_word = random_word(histogram_dictionary)
        if selected_word in test_dictionary:
            test_dictionary[selected_word] += 1
        else:
            test_dictionary[selected_word] = 1
    return test_dictionary
def file_open():
    '''Opens and then returns the file.'''
    with open('frankenstein.txt', 'r') as text:
        words = text.read().replace('\n', '').lower().split()
    return words
    
if __name__ == "__main__":
    text = file_open()
    histo = histogram(text)
    print(histo)
    print(random_word(histo))
    print(dictionary_test(histo))