def hashtag(s):
    '''Função para gerar uma string junto com a hastag no princípio no meio e nofinal'''
    'str -> str'

    a = s
    b = list(a)
    x = ' '.join(b) 

    if s == ' ':
        return '###'