def maiores(lista, n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra
    lista, que contenha todos os números da lista original maiores que n ordenados em ordem crescente;
       list, int --> list'''
    lista2 = [x for x in lista if x > n]
    lista2.sort()
    return lista2