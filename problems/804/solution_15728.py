def filtra_pares(a,b,c,d):
    """função que recebe 4 elementos de uma tupla e retorna
    uma nova tupla apenas com os elementos pares
    tupla -> tupla"""
    t=a,b,c,d
    subt=()
    if(a%2==0):
        subt=a
    if(b%2==0):
        subt=subt,b
    if(c%2==0):
        subt=subt,c
    if(d%2==0):
        subt=subt,d
    return subt