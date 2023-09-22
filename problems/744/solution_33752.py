def hashtag(s):
    ''' funcao que concatena hashtags a string dada '''
    
    x = len(s)/2
    
    if (x == int):
        return '#' + s[0:x] + '#' + s[x:] + '#'
    
    elif (x == float): 
        return '#' + s[0:floor(x)] + '#' + s[floor(x):] + '#'