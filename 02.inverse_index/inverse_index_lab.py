from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0, len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    inverseIndex = {}
    for (i, s) in enumerate(strlist):
        for w in s.split():
            if w in inverseIndex:
                inverseIndex[w] |= {i}
            else:
                inverseIndex[w] = {i}
    return inverseIndex

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    solution = set()
    for k in query:
        if k in inverseIndex:
            solution |= inverseIndex[k]
    return solution

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    isFirstItem = True
    for k in query:
        if k in inverseIndex:
            if isFirstItem:
                solution = inverseIndex[k]
                isFirstItem = False
            else:
                solution &= inverseIndex[k]
    return solution
    
