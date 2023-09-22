def maiores(lista,n):
    """retorna uma nova lista que contenha os numeros da lista original maiores que n, ordenados em ordem crescente;
    list, int -> list"""
    list.sort(lista)
    listaM=lista
    if int(listaM[:])<n:
        del listaM[:]
    return listaM