# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 23:53:29 2017

@author: knewton
"""

import re
from collections import Counter
from cube_database_connection import connect_to_database


def words(text): return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('big.txt').read()))

#print(WORDS)
def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N




def correction(word): 
    "Most probable spelling correction for word."
    print(candidates(word))
    print(word)
    return max(candidates(word), key=P)


'''def query_words():
    query="SELECT word FROM dictionary"
    all_database_words=list(connect_to_database(query))    
    
    return all_database_words
'''
all_database_words=list(connect_to_database())    

'''def query_synonyms():
    query="SELECT synonyms FROM dictionary"
    all_database_synonyms=list(connect_to_database(query)) 
    return all_database_synonyms
'''
def convert_to_string_final(final_list):
    blank_string=' '
    final_string=' '
    for times in final_list:
        final_string=final_string+times
        final_string=final_string+blank_string
    
    
    final_string=final_string[1:len(final_string)-1]  
    #print(len(final_string))
    #final_string=' '.join(final_list)
    return final_string


def dialogue_normalizer(word):
    final_list=[]
    token_list=word.split(' ')
    no_of_times=0
    for no_of_times in token_list:
        each_candidates=candidates(no_of_times)
        #print(list(each_candidates))
        for check in each_candidates:
            #print('one by one possible candidate',check)
            x=match_candidate_database(check)
            if x == 1:
                #print('matched_word=',check)
                final_list.append(check)
                #print('sub_final_list=',final_list)
                break
        if x == 0:
            final_list.append(no_of_times)
    
    final_string=convert_to_string_final(final_list)      
    return final_string   

      
def match_candidate_database(word):
    
    #all_database_words with possible shorthands
    found=0
    #print('inside match function')
    #word=set()
    #word=set(word).intersection(set(all_database_words))
    #print('intersected words....',word)
    #print(all_database_words[3])
    #all_database_words.replace(',','')
    #print(word)
    for each_word in all_database_words:
        #print('database word =',each_word,'my_word=',word)
        if each_word == word:
            found=1
            #print(found)
            return found
    
    #print ('outside match word',found)
    return found
      
def candidates(text): 
    "Generate possible spelling corrections for word."
    
    return (known([text]) or known(edits1(text)) or known(edits2(text)) or [text])



def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))













