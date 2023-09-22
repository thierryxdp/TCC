def maiores(lista_num,n):
    """Dada uma lista de numeros inteiros e um numero inteiro "n", retorna uma outra lista que contenha apenas os numeros da lista original que sejam maiores que "n" """
    """entrada: lista, int
    saida: lista"""

    list.append(lista_num,n)
    list.sort(lista_num)
    x = list.index(lista_num,n)

    return lista_num[x+1:]