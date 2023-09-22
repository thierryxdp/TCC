#
def maiores(lista_numeros,n):
    "Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n."
    return list(sorted(filter( lambda e: e >= n ,lista_numeros)))