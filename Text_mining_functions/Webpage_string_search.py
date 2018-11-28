# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:45:30 2018

@author: Gabriel T Scarlett
"""


def web_string(s, p):
    
    """
    Function to check if a phrase p is contained within a webpage s
    Both s and p are strings.
    Use requests library to get page
    Return error / true or failure
    """
    # raise an exception eror is bad status code 
    
    import requests # import the http requests library
    
    try: # try except to catch error with get request
        response = requests.get(s) # get http response for requested address 
    
        if response.status_code is not 200: # check that the query was successful
            print("Webpage not found") # if webpage is not available break and print error
        else:    
            web_string=response.content.decode('utf-8') # decode the webpage into a python string
            x=web_string.find(p) # search through the webpage string for the phase string
            if x==-1: # if -1 phrase not found
                print("Phrase not found") # lets notify
            else: # else phrase found
                print("Phrase found") # lets notify
                return x # return the location of the phrase in the string
    except:
        print('Problem with get request')
    
    
print(web_string("http://www.epicurious.com/search/Tofu+Chili","fish"))
