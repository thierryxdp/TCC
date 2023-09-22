def maiores(lista_numeros,n):
    """Função que, dada uma lista de números inteiros e um número inteiro n, retorna outra lista, contendo todos os números da lista original maiores que n, ordenados em ordem crescente
    entrada: list, int
    saída: list"""
    lista_incluida=list.append(lista_numeros,n)
    lista_ordenada=list.sort(lista_numeros)
    lista_modificada=list.index(lista_numeros,n)
    return lista_numeros[lista_modificada+1:]