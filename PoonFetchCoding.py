#!/usr/bin/env python
## This notebook shows a python program that takes in two text files and calculate the (Jaccard) similarity between them. It requires only the re package for cleaning the text. We clean the text for comparison by 1) lowercasing the words, and 2) write out shorten words like "you'll" to "you will" so that they are uniformly presented among the sample texts. Note that we do not perform any stemming/lemmatization since it will be much better handled by using the libraries like NLTK. Then  we define the function to calculate the Jaccard similarity, which is the comparing the ratio of the number of overlapping words between two texts to the total number of unique words in the text. It will have a value of 1 if the unique words between the two texts are the same and 0 if there are no words in common.

import re

def txt_to_str(file):
    with open(file, 'r') as f:
        data = f.read().replace('\n', '').lower()
        data = re.sub('don\'t', 'do not', data)
        data = re.sub('you\'ll', 'you will', data)
        data = re.sub('we\'ll', 'we will', data)
    return data

def get_jaccard_sim(str1, str2): 
    set1 = set(str1.split()) 
    set2 = set(str2.split())
    intset = set1.intersection(set2)
    return float(len(intset)) / (len(set1) + len(set2) - len(intset))

def text_sim(text1, text2):
    str1 = txt_to_str(text1)
    str2 = txt_to_str(text2)
    return get_jaccard_sim(str1,str2)

text_file_1 = input("Enter the path of the first text file : ")
text_file_2 = input("Enter the path of the second text file : ")

print('The similiarity metric between the two texts is', text_sim(text_file_1, text_file_2))