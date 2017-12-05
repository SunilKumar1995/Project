# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:43:46 2017

@author: Binary
"""

'''MODULE TO CALCULATE THE BIGRAM OF A GIVEN SET'''

import nltk

string="What is my income tax ?"
tokenised=string.split(" ")
print(nltk.bigrams(tokenised))







