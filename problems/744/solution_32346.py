from math import floor
def hashtag(s):
    posicao = floor(len(s)/2)
    return '#' + s[:posicao] + '#' + s[posicao:] + '#'