def hashtag(s):
    '''Insere uma # no início, meio e fim de uma string de entrada
    str -> str'''
    x = len(s)
    return '#' + s[:x//2] + '#' + s[(x//2)-1:]