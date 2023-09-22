def filtra_pares(numeros):
    """Retorna os elementos inteiros e pares de uma tupla.
       int,int,int,int => int,int,int,int"""
    [a1,a2,a3,a4] = numeros
    par = ()
    
    if a1 % 2 == 0:
        par = (*par, a1)
    if a2 % 2 == 0:
        par = (*par, a2)
    if a3 % 2 == 0:
        par = (*par, a3)
    if a4 % 2 == 0:
        par = (*par, a4)
    
    return par