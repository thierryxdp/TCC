def maiores(lista_numero, n):
    """A função recebe uma lista de numeros inteiros e um numero inteiro n,
    e retorna uma outra lista, que contenha todos os numeros da lista original
    maiores que n;
    list, int - list"""
    list.append(lista_numero, n)
    list.sort(lista_numero)
    ocorrencia = list.index(lista_numero, n)+1
    return lista_numero[ocorrencia:]