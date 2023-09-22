def filtra_pares(x):
    """retorna uma tupla contendo somente os elemetos pares da tupla original, na mesma ordem que se encontravam.
    tpl->tlp"""
    a,b,c,d=x
    resultado=()
    
    if a%2==0:
        resultado+=(a,)        
    if b%2==0:
        resultado+=(b,)
    if c%2==0:
        resultado+=(c,)
    if d%2==0:
        resultado+=(d,)
    
    return resultado