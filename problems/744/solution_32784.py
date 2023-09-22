def hashtag(s):
    '''Função para gerar uma string junto com a hastag no princípio no meio e nofinal'''
    'str -> str'

    a = s
    b = list(a)
    x = ' '.join(b)
    y = '#'

    if s == '':
        return 3 * y
    if s == s[0]:
        return y + s[0] + y + y