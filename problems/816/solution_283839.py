def maiores(lista,n):
    """ Função que dada uma lista, retorna outra lista contendo todos os números da lista original maiores que n, ordenados em ordem crescente 
    list,int -> list """
    list.append(lista,n)
    list.sort(lista,n)
    lista=lista[n:]
    return lista