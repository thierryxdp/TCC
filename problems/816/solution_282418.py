def maiores(lista, n):
    """Função que retorna uma lista ordenada com os números maiores que n fornecidos"""
    list.insert(lista,0,n)
    list.sort(lista)
    posicao= list.sort(lista,n)
    lista2 = lista[posicao+1:]
    return lista2