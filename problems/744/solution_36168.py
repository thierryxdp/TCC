from math import floor
def hashtag(s):
    '''retorna uma string  com '#' intercaladas( no início, meio, e fim);
    string->string'''
    metade= floor(len(s)/2)
    return '#'+s[0:metade]+'#'+s[metade:]+'#'