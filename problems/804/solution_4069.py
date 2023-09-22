def filtra_pares(tupla):
    pares= ()
    if tupla[1]%2==0:
        pares= pares + (tupla[1])
    elif tupla[2]%2==0:
        pares= pares + (tupla[2])
    elif tupla[3]%2==0:
        pares= pares + (tupla[3])
    elif tupla[4]%2==0:
        pares= pares + (tupla[4])
        return pares