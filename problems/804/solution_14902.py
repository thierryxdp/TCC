def filtra_pares(v1,v2,v3,v4):
    valores_lista=(v1,v2,v3,v4)
    return tuple(filter(lambda x: x%2==0, valores_lista))