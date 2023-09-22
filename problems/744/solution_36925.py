def hashtag(s):
    '''função que recebe uma string e insere # no início, meio e fim'''
    'str -> str'
    if len(s)%2==0:
        pausa=len(s)//2
        else:
            pausa=len(s)//2
        return '#'+s[:pausa]+'#'+s[pausa:]+'#'