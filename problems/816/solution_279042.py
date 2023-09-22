def maiores(lista_numeros,n):
    """uhahauhdha"""
    lista_vazia = []
    list.extend(lista_vazia,lista_numeros)
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    for i in lista_numeros:
        if i > n:
            return list(i)