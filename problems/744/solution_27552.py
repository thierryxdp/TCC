def hashtag(s):
    
    metade = int(len(s)/2)
    
    return '#' + s[:metade] + '#' + s[0 + metade:] + '#'