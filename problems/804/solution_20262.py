def filtra_pares(a,b,c,d):
    pares=tuple()
    
    if a%2==0:
        pares+=(a,)
    if b%2==0:
        pares+=(b,)
    if c%2==0:
        pares+=(c,)
    if d%2==0:
        pares+=(d,)
        
    lista_valida= filter(pares)
    return lista_valida