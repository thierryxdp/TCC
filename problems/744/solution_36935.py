def hashtag(s):
    '''função que recebe uma string e insere # no inicio, no meio e no fim'''
    'str -> str'
    if len(s)%2==0:
        pausa=len(s)//2
    else:
        pausa=(len(s)-1)//2
    return '#'+s[:pausa]+ '#'+s[pausa:]+'#'