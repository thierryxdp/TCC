from math import *

def hashtag(s):
    '''função que retorna a string inserida s com um caractere hashtag "#"
    no início, meio e final
    str -> str'''
    return '#' + s[:floor(len(s)/2)] + '#' + s[floor(len(s)/2):] + '#'