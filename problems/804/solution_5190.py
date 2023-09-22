def filtra_pares(tupla):
    pares=()
    proximo=0
    while proximo<len(tupla):
        if tupla[proximo]%2==0:
            pares=pares+tupla[proximo]
        proximo=proximo+1
    return pares