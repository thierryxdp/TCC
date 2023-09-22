def maiores(lista_numeros,n):
    """Essa função retorna uma lista com os números maiores que n.
    Como entrada temos uma lista de números e um valor inteiro n, e
    como saída temos uma lista nova com os números maiores que n"""
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    lista_maiores=lista_numeros[n+1:]
    return lista_maiores