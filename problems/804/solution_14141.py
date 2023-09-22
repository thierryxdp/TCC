def filtra_pares(tupla):
    tuplaN= ()
    if tupla[0] % 2 == 0:
        tuplaN = tuplaN + (tupla[0],)
    elif tupla[1] % 2 == 0:
        tuplaN = tuplaN + (tupla[1],)
    elif tupla[2] % 2 == 0:
        tuplaN= tuplaN + (tupla[2],)
    elif tupla[3] % 2 ==0:
        tuplaN = tuplaN + (tupla[3],)
    
    return tuplaN