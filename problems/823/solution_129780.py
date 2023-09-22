def faltante(L):
    """Retorna o inteiro que indica a peca faltante.list-->int"""
    i=0
    while L[i]+1==L[i+1]:
        termo_faltante=L[i]
        i=i+1
        return termo_faltante