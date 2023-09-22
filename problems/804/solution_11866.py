def filtra_pares(tupla):
    elementos_pares = ()
    
    if tupla[0] % 2 == 0:
        elemntos_pares = elementos_pares + (tupla[0],)
    if tupla[1] % 2 == 0:
        elementos_pares = elementos_pares + (tupla[1],)
    if tupla[2] % 2 == 0:
        elementos_pares = elementos_pares + (tupla[2],)
    if tupla[3] % 2 == 0:
        elementos_pares = elementos_pares + (tupla[3],)
        
    return elementos_pares