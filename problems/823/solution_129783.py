def faltante(L):
    """Retorna o inteiro que indica a peca faltante.list-->int"""
    i=0
    if L[0]!=1:
        termo_faltante=1
    else:
        while L[i]+1==L[i+1]:
        termo_faltante=L[i]+1
        i=i+1
        return termo_faltante