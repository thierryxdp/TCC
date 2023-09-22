def hashtag(s):
    '''essa funcao modifica'''
    '''str-> str'''
    j = s[0:math.floor(len(s)/2)]
    k = s[math.floor(len(s)/2):len(s)]
    return '#' + j + '#' + k + '#'