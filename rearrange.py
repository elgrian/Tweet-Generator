import random
import sys
#Takes words given as an argument in CL, which then randomises the words
def random_word():
    word_list = sys.argv[1:] 
    random_word_list = []
    
    for i in word_list:
        rand_index = random.randint(0, len(word_list) -1)
        list = word_list[rand_index]
        random_word_list.append(list)
        string = ' '.join(random_word_list)
    return string
    
    
    
    # random_word()
if __name__ == '__main__':
    random = random_word()
    print(random)