# import tuples, re, sys
# words = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
# frequency = [1, 4, 1, 4, 1, 4, 1, 4]
# denominator = int(len(words))
# frequency_percent = []
# for i in frequency:
#     frequency_percent.append((i / denominator))
# 
# print(str((frequency_percent)))
# 
# 



# 
# take dictionary and iterate through it, taking the value of each key, and dividing it by the length of the text file.
# Then replacing the original keys value with the new "percent float".  
# Which keeps them still in a dictionary, which we can now find a way to call on those words based on their "percent float"

import re, random, sys, numpy as np


frequency = {}
first_list = []
second_list = []
document_text = open('example.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
    first_list.append(word)

for word in match_pattern:
    second_list.append(int(frequency[word]))    
zipped = zip(first_list, second_list)
dictionary = (list(set(zipped)))
new_dictionary = dict(dictionary)
# print(dict(dictionary))
# print(zipped)

# dict_word = new_dictionary.keys()
for i in new_dictionary:
    new_dictionary[i] = (new_dictionary[i] / len(match_pattern))
    # print(new_dictionary[i])
    dict.update(new_dictionary)
     
    
#     >>> books = {}
# >>> books['book'] = 3       
# >>> books['book'] -= 1   
# >>> books   
# {'book': 2} 
# number_thing = 0
# eight = 8
# while number_thing < eight:

new_dict_words = list(new_dictionary.keys())
new_dict_weight = list(new_dictionary.values())

# print(random.choices(list(new_dictionary)), list(int(new_dictionary[i])), k = 8)
#     number_thing += 1
    
    
# print(new_dictionary)
# choice_list = np.random.choice(new_dict_words, 8, replace = True, p = new_dict_weight)
# print(choice_list)

# weighted_random_by_dct(new_dictionary)
def frequency_test():
    i = 0
    blue = 0
    fish = 0
    red = 0
    two = 0
    one = 0

    while i <= 10000:
        selection = choice_list = np.random.choice(new_dict_words, 1, replace = True, p = new_dict_weight)
        if 'blue' in selection:
            blue += 1
            i += 1
        elif 'fish' in selection:
            fish += 1
            i += 1
        elif 'red' in selection:
            red += 1
            i += 1
        elif 'two' in selection:
            two += 1
            i += 1
        elif 'one' in selection:
            one += 1
            i += 1
            
    print("Blue => " + str(blue) + "\n fish => " + str(fish) + "\n red => " + str(red) + "\n two => " + str(two) + "\n one => " + str(one))

frequency_test()
# print(new_dictionary)
# 
# print (new_dictionary)
# 
# print(len(text_string))
# 
# print(89 / 75150)
# 
# print(len(new_dictionary))
# 
# print(new_dictionary)




# for i in numbers:  Go through the zipped list_of_tuples
#     for i in second_list, take that number and divide it by the amount of number of words said overall
#     i = x / y
#     THEN
#     OVERRIGHT****.remove() THEN .append()****frequency_number, with i, in second_list, replacing the old number with a percentage of frequency
# 
# 
     