def filtra_pares(lista):
    lista_nova=[]
    lista_pares=[termo for termo in lista if termo %2 ==0]
    lista_nova.append(lista)
    return lista_nova