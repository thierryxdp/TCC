def concatenacao(a, b):
    '''Função que retorna a concatenação das strings a e b; string -> string'''
    if (a) and (b):
        return str(a)+str(b)+str(b)+str(a)
    if (a):
        return str(a)
    if (b):
        return str(b)