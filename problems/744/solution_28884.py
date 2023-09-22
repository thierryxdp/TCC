def hashtag(s):
    ''' Retorna o caractere "#" no início, no meio e no
        final da string(s)
        str -> str
    '''
    metade = int(len(s)/2)
    return '#'+s[0:metade]+'#'+s[metade:]+'#'