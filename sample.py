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

import re, random, sys

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


for i in new_dictionary:
    new_dictionary[i] = (new_dictionary[i] / len(match_pattern))
    dict.update(new_dictionary)
    
    
#     >>> books = {}
# >>> books['book'] = 3       
# >>> books['book'] -= 1   
# >>> books   
# {'book': 2} 
# print(random.choices(list(new_dictionary)))
print(new_dictionary)

# print (new_dictionary)

# print(len(text_string))
# 
# print(89 / 75150)
# 
# print(len(new_dictionary))

# print(new_dictionary)




# for i in numbers:  Go through the zipped list_of_tuples
#     for i in second_list, take that number and divide it by the amount of number of words said overall
#     i = x / y
#     THEN
#     OVERRIGHT****.remove() THEN .append()****frequency_number, with i, in second_list, replacing the old number with a percentage of frequency
# 
# 
     