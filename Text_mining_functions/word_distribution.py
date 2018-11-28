# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:37:35 2018

@author: Gabriel T Scarlett
"""

def word_distribution(s, word_list = None):
    
    """
    Take input string s and return a dictionary with the count of each word in 
    it with all punctuation removed.
    """

    #
    # YOUR CODE HERE
    #
    wordcount={} # initialise an empty dictionary
    s=s.lower()  # convert all upper case letters to lower
    myList=s.split() # split string by spaces and place words into a list
    for word in myList: # iterate over the list
            newWord="".join([i for i in word if i.isalpha()]) # remove non-alphabetical characters
            count=1 # initialise a counter
            for key in wordcount: # iterate overs keys in the dictionary
                if key==newWord: # if the word is already in the dictionary add to count
                    count+=1
            wordcount[newWord]=count          
            
    
    return wordcount

# test function
word_distribution("Hello. My name is Gabriel. What's your name?") 
word_distribution("This function assumes that all words are words (if you get me)!")