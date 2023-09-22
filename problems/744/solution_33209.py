import math
def hashtag(s):
    '''Insere o caracter # no inicio,no meio e no final da
    palavra;
    str-> str'''
    i=len(s)
    return str('#'+s[:i]+'#'+s[i+1:]+'#')