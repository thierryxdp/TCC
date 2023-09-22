def hashtag(s):
    '''Recebe uma string e retorna com '#' no início, no meio e no final.
    str->str'''
    x=s
    y=len(x)
    z=int((y//2))
    return '#'+x[0:z]+'#'+x[z:]+'#'