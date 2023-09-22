def hashtag(s):
    '''
    retorna uma string s com caracteres # inseridos no inicio
    meio e fim
    str->str
    '''
    return '#'+s[0:(ceil(len(s)/2))]+'#'+s[(ceil(len(s)/2)):len(s)]+'#'