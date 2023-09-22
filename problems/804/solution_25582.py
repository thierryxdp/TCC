def filtra_pares(x,y,a,b):
    """
    Função que dados 4 numero inteiros, retorna em uma tupla apénas aqueles
    que são pares, na respectiva ordem.
    """
    f = (x,y,a,b)
    p = ()
    if f[0] % 2 ==0:
        p = (*p, f[0])
    if f[1] % 2 ==0:
        p = (*p, f[1])
    if f[2] % 2 ==0:
        p = (*p, f[2])
    if f[3] % 2 ==0:
        p = (*p, f[3])
    return p