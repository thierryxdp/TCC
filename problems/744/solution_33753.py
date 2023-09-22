def hashtag(s):
    ''' funcao que concatena hashtags a string dada '''
    
    x = len(s)/2
    
    if (x%2 == 0):
        return '#' + s[0:x] + '#' + s[x:] + '#'
    
    elif (x%2 == 1): 
        return '#' + s[0:floor(x)] + '#' + s[floor(x):] + '#'