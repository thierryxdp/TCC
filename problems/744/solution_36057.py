import math
def hashtag(s):
    '''retorna a sting s com o caracter # inserido no início, no meio e
    no final; str -> str'''
    antes=s[:math.floor(len(s)/2)]
    depois=s[math.floor(len(s)/2):]
    return '#'+antes+'#'+depois+'#'