def hashtag(s):
    '''str-> str'''
    j = s[0:s.floor(len(s)/2)]
    k = s[s.floor(len(s)/2):len(s)]
    
    return '#' + j + '#' + k + '#'