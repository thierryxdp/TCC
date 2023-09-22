def filtra_pares(v0,v1,v2,v3):
    valores_lista=[v0,v1,v2,v3]
    pares = list(filter(lambda x: x%2==0, valores_lista))
    return (pares)