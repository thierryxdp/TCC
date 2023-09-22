def filtra_pares(tupla):
   tuplaN= ():
    if tuplaN[0] % 2 == 0:
        tuplaN = tuplaN + ( tupla[0],)
    if tuplaN[1] % 2 == 0:
        tuplaN = tuplaN + ( tupla[1],)
    if tuplaN[2] % 2 == 0:
        tuplaN = tuplaN + ( tupla[2],)
    if tuplaN[3] % 2 == 0:
        tuplaN = tuplaN + ( tupla[3],)
        
    return tuplaN