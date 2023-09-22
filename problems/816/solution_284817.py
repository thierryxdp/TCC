def maiores(lista,n):
    '''função que dada uma lista de inteiros e um número inteiro n, retorna outra lista que contenha todos os números dessa lista original maiores que n, ordenados em ordem crescente    ent-> (lista, int)     saida-> lista '''
    
	listan = [n]
    listatotal = listan + lista
    list.sort(listatotal)
    return listatotal