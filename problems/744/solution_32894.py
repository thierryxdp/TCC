def hashtag(s):
    '''
    '''
    i = len(s)//2
    return "#" + s[0:i] + "#" + s[i-1:] + "#"