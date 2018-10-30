import random
import sys
#Takes words given as an argument in CL, which then randomises the words
def random_word():
    word_list = sys.argv[1:] #Can also use sys.argv[1:len(sys.argv)]
    random_word_list = []
    
    for i in word_list: # while len(word_list) is not or > 0:  <-- I really liked this
        rand_index = random.randint(0, len(word_list) - 1) #Could also do random.randrange(len(word_list))
                                    #This line would swap the random index with the last element
        list = word_list[rand_index]# word_list[i], word_list[-1] = world_list[-1], word_list[i]
        #Could use rand_word = word_list.pop()
        random_word_list.append(list)# Could also use result.append(rand_word)
        string = ' '.join(random_word_list) #Could also print( " ".join(random_word_list))
    return string

    
    
    
    # random_word()
if __name__ == '__main__':
    random = random_word()
    print(random)
    
    
    #del array[*Random array location*] - append before del because "del" deletes it completelyself. 