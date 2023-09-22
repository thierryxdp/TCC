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
        return y + y + s[0] + y
    if s == s[1]:
        return y + s[0]+ y + s[1] + y
    if s == s[3]:
        return y + s[0] + y + s[1] + s[2:] + y