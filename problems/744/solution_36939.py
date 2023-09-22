"""Dada um string a função adiciona # no início, meio e fim dela"""
def hashtag(s):
    j = s[0:math.floor(len(s)/2)]
    k = s[math.floor(len(s)/2):len(s)]
    return '#' + j + '#' + k + '#'