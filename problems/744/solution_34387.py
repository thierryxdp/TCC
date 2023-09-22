def hashtag(s):
    '''adiciona o caractere # no início, meio e fim de uma string de entrada
    str -> str'''
    x = len(s)
    h = '#' + s[:x/2] + '#' + s[(x/2)-1:]
    return h