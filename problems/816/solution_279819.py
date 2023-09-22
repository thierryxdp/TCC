def maiores(lista1,n):
    '''função dada uma lista de números inteiros e um número inteiro n, retorna outra lista
    que contenha todos os números da lista original maiores que n:
    str, int -> str'''
    l= lista1
    a= [b for b in l if b > n]
    x= a.sort()
    return a