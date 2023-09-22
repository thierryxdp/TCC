def hashtag(s):
    '''adiciona o caractere # no início, meio e fim de uma string de entrada
    str -> str'''
    x = len(s)
    y = x/2
    h = '#' + s[:y] + '#' + s[y-1:]
    return h