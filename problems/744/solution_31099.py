def hashtag(s):
    '''Funcao que recebe string s
    e retorna a mesma com '#' no
    inicio, meio e fim.'''
    meio = len(s)//2
    return '#' + s[0:meio]+'#' + s[meio:] + '#'