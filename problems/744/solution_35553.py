from math import floor
def hashtag(s):
   
    
     meio = floor(len(s) / 2)
 return '#' + s[0:meio] + '#' + s[meio:] + '#'