def filtra_pares(lista):
    lista_nova=[]
    lista_pares=[termo for termo in lista if termo %2 ==0]
    lista_nova.append(lista_pares)
    lista_filtrada=tuple(lista_pares)
    return lista_filtrada