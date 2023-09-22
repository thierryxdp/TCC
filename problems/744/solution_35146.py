import math
def hashtag(s):
    '''função que tem como entrada uma string e retorna essa mesma string acrescida de "#" no começo, meio e fim.'''
    string = s
    m = math.floor((len(s)/2))
    return '#' + s[:m] + '#' + s[m:] + '#'