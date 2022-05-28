# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

from collections import Counter
from itertools import count




def find_anagram(word, anagram):

     
    if(Counter(word)== Counter(anagram)):
        return True
    else:
        return False