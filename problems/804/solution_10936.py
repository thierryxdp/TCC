def filtra_pares(t):
    '''Função que retorna apenas os elementos pares da tupla que contém quatro elementos inteiros.
    tupla(int,int,int,int)->tupla'''
    if(t[0]/2==t[0]//2):
        a=(t[0],)
    else:
        a=0
    if(t[1]/2==t[1]//2):
        b=(t[1],)
    else:
        b=0
    if(t[2]/2==t[2]//2):
        c=(t[2],)
    else:
        c=0
    if(t[3]/2==t[3]//2):
        d=(t[3],)
    else:
        d=0
    return a+b+c+d