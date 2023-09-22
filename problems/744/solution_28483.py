def hashtag(s):
    ''' Recebe uma string e insere "#" no início no meio e no fim dela;
    str-> str'''
    x=len(s)//2
    return '#'+s[0:x]+'#'+s[x:]+'#'