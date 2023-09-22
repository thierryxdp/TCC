def maiores(lista_inteiros, n):
    """dada uma lista de números inteiros e um número inteiro n, a função retorna outra lista que contenha todos os
    números da lista original maiores que n; list, int -> list"""
    if n in lista_inteiros:
        list.sort(lista_inteiros)
        indice = list.index(lista_inteiros, n)
        return lista_inteiros[indice+1:]
    if n not in lista_inteiros:
        lista_inteiros[0:0] = [n]
        list.sort(lista_inteiros)
        indice = list.index(lista_inteiros, n)
        return lista_inteiros[indice+1:]