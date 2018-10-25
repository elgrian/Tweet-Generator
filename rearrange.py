import random
import sys

def random_word():
    word_list = sys.argv[1:]
    random_word_list = []
    for i in word_list:
        rand_index = random.randint(0, len(word_list) -1)
        list = word_list[rand_index]
        random_word_list.append(list)
        str1 = ' '.join(random_word_list)
    return str1
    
    
    
    # random_word()
if __name__ == '__main__':
    random = random_word()
    print(random)