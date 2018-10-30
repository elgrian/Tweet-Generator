import re
# import string

def run_histogram():
    frequency = {}
    first_list = []
    second_list = []
    document_text = open('frankenstein.txt', 'r')
    text_string = document_text.read().lower()
    match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
    
    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
        first_list.append(word) #Appends the word to the first list
    #Adds number of times word was repeated to second array
    for word in match_pattern:
        second_list.append(int(frequency[word]))    
    zipped = zip(first_list, second_list)
    print(list(set(zipped)))
    
if __name__ == '__main__':
    run_histogram()