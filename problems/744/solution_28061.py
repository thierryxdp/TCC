def hashtag(s):
    '''Retorna um texto com o caracter "#" no meio fim e incio do mesmo
    str --> str '''
    return '#' + s[0:(len(s)//2)] + '#' + s[(len(s)//2):len(s)] + '#'