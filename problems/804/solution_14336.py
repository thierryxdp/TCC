def filtra_pares(tupla):
    tuplaN=()
    if tupla[0]%2==0:
        tuplaN=tuplaN+(tupla[0],)
    if tupla[1]%2==0:
        tuplaN=tuplaN+(tupla[1],)
        return tuplaN