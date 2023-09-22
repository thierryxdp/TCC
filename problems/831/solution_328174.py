def lingua_p(p):
    ''' Função que converte palavras em português p em palavras da lingua do P.'''
    d=list(p)
    f=list(p)
    j=0
    for i in d:
        if (i!='qwrtypsdfghjlçzxcvbnm'):
            f[j:j]='p'+d[j]
        j=j+1
    return str.join('',f)