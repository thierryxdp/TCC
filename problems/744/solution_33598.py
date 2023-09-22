import math
def hashtag(s):
    '''retorna a string com # no começo, meio e fim;
     str->str'''
    variavel=math.floor((len(s)/2))
    return "#" + s[:variavel] + "#" + s[variavel:] + "#"