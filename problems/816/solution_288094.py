def maiores(lista,n):
    '''dada uma lista de números inteiros e um número inteiro n, retorna outra lista com todos os números da lista original maiores 
    que n, em ordem crescente. list, int-> list''' 
    if n in lista:
        list.sort(lista)
        return lista[list.index(lista,n)+1:]
    list.append(lista,n)
    list.sort(lista)
    return lista[list.index(lista,n)+1:]