import random, timeit
from sys import argv
#Creates a variable for the counter
i = 0
argument_int = int(argv[1])

def load_word():
    """Reads the words from a dictionary"""
    f = open("words.txt", 'r')
    words_list = f.readlines() 
    f.close()
    split_words = words_list[0].split(' ')
    return split_words
    
    
def choose_word(words_list):
    # choosing random word from words.
    random_word = random.choice(words_list)
    return random_word
#While i is less than the int made in the argument, loop while adding 1 to i for each loop
load_the_words = load_word()


if __name__ == "__main__":
    while i < argument_int:
        print(choose_word(load_the_words))
        i += 1





    

    
        

        
