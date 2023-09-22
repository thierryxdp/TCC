from math import *
def hashtag(s):
    ''' funcao que concatena hashtags a string dada '''
    
    x = len(s) % 2
    
    if (x == 0):
        
        y = (len(s))/2
        
        return '#' + s[0:y] + '#' + s[y:] + '#'
    
    elif (x == 1):
        
        y = (len(s))/2
        z = floor(y)
        
        return '#' + s[0:z] + '#' + s[z:] + '#'