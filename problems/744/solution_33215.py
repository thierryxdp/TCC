import math
def hashtag(s):
    '''Insere o caracter # no inicio,no meio e no final da
    palavra;
    str-> str'''
    i=len(s)
    p=math.ceil(i//2)
    return str('#'+s[:p]+'#'+s[p+1:]+'#')