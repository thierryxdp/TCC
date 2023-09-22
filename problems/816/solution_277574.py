def maiores(lista, n):
	'''Dada uma lista de n ́umeros inteiros e um n ́umero inteiro n, retorna
    outra lista, que contenha todos os n ́umeros da lista original maiores 
    que n. lista,int -> lista'''
    return [i for i in lista if i > n]