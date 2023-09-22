def filtra_pares(a):
    pares, impares= separa(a)
    pares=tuple(it for it in valores if it[0]%2==0)
    return pares