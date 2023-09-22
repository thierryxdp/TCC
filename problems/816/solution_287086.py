def maiores(lista,n):
    """Retornar uma função em que dada uma lista de n°'s inteiros e um n° inteiro n, retorne outra lista, com todos os n°'s da lista original maiores que n, além de ordenados e na ordem crescente;list,inte=>list"""
	if n in lista:
    	list.sort(lista)
    	outra_lista = list.index(lista,n)
    	return lista[outra_lista+1:]
    else:
        list.append(lista,n)
        list.sort(lista)
        lista_1 = list.index(lista,n)
        return lista[outra_lista+1:]