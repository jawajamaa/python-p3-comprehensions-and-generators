#!/usr/bin/env python3
num_list = ([0, 1, 3, 5, 7, 8, 9])

def return_evens(num_list):
    even_nums = [n for n in num_list if (n % 2 == 0)]
    if even_nums == []:
        return []
    else:    
        return even_nums

return_evens(num_list)

sentence_list = (["Hello", "I'm doing great", "Python is fun"])

def make_exclamation(sentence_list):
    if sentence_list == []:
        return []
    else:
        exclamations = [n + "!" for n in sentence_list if True ]
        return exclamations

make_exclamation(sentence_list)
