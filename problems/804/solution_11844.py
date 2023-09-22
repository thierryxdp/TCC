def filtra_pares([t]):
    elementos_pares = ()
    
    if t[0] % 2 == 0:
        elemntos_pares = elementos_pares + (t[0], )
    if t[1] % 2 == 0:
        elementos_pares = elementos_pares + (t[1], )
    if t[2] % 2 == 0:
        elementos_pares = elementos_pares + (t[2], )
    if t[3] % 2 == 0:
        elementos_pares = elementos_pares + (t[3], )
        
    return elementos_pares