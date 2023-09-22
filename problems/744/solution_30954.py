def hashtag(s):
    '''Adiciona # numa no início, meio e fim de uma string (s)
    str-> str'''
    T = len(s)
    return '#' + s[0:(T//2)] + '#' + s[T//2: ] + '#'