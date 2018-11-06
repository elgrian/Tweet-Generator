import random
import re
first_list = []
second_list = []
# histogram_tuple = []
frequency = {}
def histogram(text):
    # for word in text:
    #     frequency_word = text.count(word)
    #     histogram_tuple.append((word, frequency_word))
    #     new_list = histogram_tuple
    #     # text_string_count = len(text_string)
    # return (new_list)
    for word in text:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
        first_list.append(word)
    
    for word in text:
        second_list.append(int(frequency[word]))
    
    # zipped = zip(first_list, second_list)
    # return (list(set(zipped)))
    # accum = 0
    # sum_tuple = sum(frequency_word)
    # random_sum = random.randint(0, sum_tuple - 1)
    # 
    # for word, frequency in histogram_tuple:
    #     accum += frequency
    #     if accum > random_sum:
    #         return word
    #     else:
    #         continue
    denominator = int(len(text))
    # n = random.randrange(0, denominator)
    accum = 0
    sum_tuple = sum(second_list)
    random_sum = random.randint(0, sum_tuple - 1)
    for i in first_list, second_list:
        accum += int(str(second_list[i]))
        if accum > random_sum:
            return first_list
        else:
            continue

    
    
def file_open():
    '''Opens and then returns the file.'''
    with open('example.txt', 'r') as text:
        # text_string = text.read().replace('\n', '').lower().split() #Not sure if .replace is necessary due to the regex
        text_string = text.read().lower()
        match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
        text_string_count = len(text_string)
    return match_pattern
    
if __name__ == "__main__":
    text = file_open()
    histo = histogram(text)
    print(histo)
    
    
    
    
    