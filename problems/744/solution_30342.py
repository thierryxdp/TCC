def hashtag(s):
    '''Função que recebe a string (s) e
    retorna a string com # no inicio, meio e fim'''
    metade=len(s)//2
    return '#' +s[0:metade]+'#'+s[metade:]+'#'