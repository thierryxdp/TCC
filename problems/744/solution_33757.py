from math import *
def hashtag(s):
    ''' funcao que concatena hashtags a string dada '''
    
    x = len(s)/2
    
    y = x%2
    
    z = floor(x)
    
    if (y == 1):
        return '#' + s[0:z] + '#' + s[z:] + '#'
    
    elif (y == 0):
        return '#' + s[0:z] + '#' + s[z:] + '#'