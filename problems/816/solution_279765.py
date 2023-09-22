def maiores(lista,n):
    """funcao que retorna apenas os numeros maiores que um n dado de uma dada lista; lista->lista """
    list.insert(lista,0,n)
    list.sort(lista)
    posicao=list.index(n)
    return lista[posicao:]