def filtra_pares(p):
    valores_lista=(p[0],p[1],p[2],p[3])
    pares= tuple(filter(lambda p: p%2==0, valores_lista))
    return pares