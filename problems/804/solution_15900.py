def filtra_pares(p):
    v1=p[1]
    v2=p[2]
    v3=p[3]
    v4=p[4]
    
    valores_lista=(v1,v2,v3,v4)
    pares= tuple(filter(lambda x: x%2==0, valores_lista))
    return (pares)