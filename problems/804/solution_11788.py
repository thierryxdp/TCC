def filtra_pares(t):
    elementos_pares = ()
    
    if t[0] % 2 == 0:
        elemntos_pares = elementos_pares + t[0]
    elif t[1] % 2 == 0:
        elementos_pares = elementos_pares + t[1]
    elif t[2] % 2 == 0:
        elementos_pares = elementos_pares + t[2]
    elif t[3] % 2 == 0:
        elementos_pares = elementos_pares + t[3]
        
    return elementos_pares