import random, timeit
from sys import argv

i = 0
argument_int = int(argv[1])
def load_word():
    # choosing random word from words.
    f = open("words.txt", 'r')
    words_list = f.readlines() 
    f.close()
    split_words = words_list[0].split(' ')
    random_word = random.choice(split_words)
    return random_word
#While i is less than the int made in the argument, loop while adding 1 to i for each loop
while i < argument_int:
    print(load_word())
    i += 1





    

    
        

        
