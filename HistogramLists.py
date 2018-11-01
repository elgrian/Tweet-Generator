import re


frequency = {}
first_list = []
second_list = []
document_text = open('frankenstein.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
    first_list.append(word)
    # first_list.append(int(frequency[word])) 
    
for word in match_pattern:
    first_list.append(int(frequency[word]))
    second_list.append(first_list)
#     second_list.append(int(frequency[word]))    
# zipped = zip(first_list, second_list)
# dictionary = (list(set(zipped)))
# 
print(str(second_list))
# 
# def unique_words():
#     print('The amount of unique words in this text file is: ' + str(len(dictionary)))
# 
# 
# 
# 
# 
# if __name__ == '__main__':
# 
#     unique_words()
