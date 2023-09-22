def maiores(lista_numeros,n):
    """uhahauhdha"""
    lista_vazia = []
    list.extend(lista_vazia,lista_numeros)
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    x = lista_numeros[n]
    del lista_numeros[:x]
    return lista_numeros