def maiores(lista: list, n: int)-> list:
    """Dada uma lista de números inteiros e um número inteiro "n",
    a função retorna outra lista com todos os números da lista original
    maiores que "n"."""
    list.append(lista, n)
    list.sort(lista)
    posicao = list.index(lista, n)
    return lista[posicao+1:]