def maiores(lista,n):
    '''função que dada uma lista de números inteiros e um número inteiro (n), retorna outra lista, que contenha todos os números da lista original maiores que (n), ordenados em ordem crescente; list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    p=list.index(lista,n)
    return lista[p+1:]