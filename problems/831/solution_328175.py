def lingua_p(p):
    ''' Função que converte palavras em português p em palavras da lingua do P.'''
    d=list(p)
    f=''
    j=0
    for i in d:
        f=f+i
        if (i!='qwrtypsdfghjlçzxcvbnm'):
            f=f+'p'+i
     
    return f