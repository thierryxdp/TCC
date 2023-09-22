def hashtag(s):
    '''Recebe uma string(s) e retorna a mesma string com # no inicio, meio e fim dela.
    string ->string'''
    metade= (len(s)//2)
    return '#'+ s[0:metade]+'#'+s[metade:]+'#'