from math import floor
def hashtag(s):
    '''
    retorna uma string s com caracteres # inseridos no inicio
    meio e fim
    str->str
    '''
    return '#'+s[0:(floor(len(s)/2))]+'#'+s[(floor(len(s)/2)):len(s)]+'#'