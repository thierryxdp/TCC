def hashtag(s):
    '''
    insere # no início, no meio e no fim de uma string.
    str->str
    '''
    return '#'+s[0:(len(s)//2)]+'#'+s[len(s)//2:]+'#'