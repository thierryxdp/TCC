import math
def hashtag(s):
    '''retorna a string s adicionada do caractere # no início, meio e final; string->string'''
    if len(s)%2=0:
        return '#'+ s[0:len(s)/2]+'#'+s[len(s)/2:]+'#'
    else:
        return '#'+ s[0:mat.ceil(len(s)/2)]+'#'+s[math.ceil(len(s)/2):]+'#'