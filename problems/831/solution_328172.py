def lingua_p(p):
    ''' Função que converte palavras em português p em palavras da lingua do P.'''
    d=list(p)
    f=list(p)
    for i in d:
        if (d[i-1]!='qwrtypsdfghjlçzxcvbnm'):
            f[i:i]='p'+d[i]
    return f