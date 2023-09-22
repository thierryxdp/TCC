def maiores (lista, n):
    """Funcao que dada uma lista de números interios e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n, lista,int->list"""
    list.append(lista,n)
    list.sort(lista)
    posicao= list.index(lista,n)
    return lista[posicao+1:]