def filtra_pares(x):
    """Retorna somente elementos pares dado uma tupla;
    tupla -> tupla"""
    a,b,c,d = x 
    resultado = ()
    
    if a%2==0 :
        resultado+=(a,)
    if b%2==0 :
        resultado+=(b,)
    if c%2==0 : 
        resultado+=(c,)
    if d%2==0 : 
        resultado+=(d,)
    return resultado