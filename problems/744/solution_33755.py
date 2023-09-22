from math import *
def hashtag(s):
    ''' funcao que concatena hashtags a string dada '''
    
    x = len(s)/2
    y = x%2
    
    if (y == 0):
        return '#' + s[0:x] + '#' + s[x:] + '#'
    
    elif (y == 1):
        
        z = floor(x)
        
        return '#' + s[0:z] + '#' + s[z:] + '#'