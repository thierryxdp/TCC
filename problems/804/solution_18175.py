def filtra_pares(tupla):
    
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
    
    return ((x for x in tupla if x%2==0))