def filtra_pares(tupla,tuplaN):
    tupla=(0,)
    tuplaN=(0,)
    if tupla[0]%2==0:
        return tuplaN
    if tupla[1]%2==0:
        return tuplaN+(tupla[0],)