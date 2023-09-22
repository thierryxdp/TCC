def hashtag(s):
    ''' a função recebe uma string e retorna '#' no inicio, no meio e
    e no fim dela
    str->str
    '''
    return '#'+s[0:len(s)//2]+'#'+s[(len(s)//2):]+'#'