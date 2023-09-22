def maiores(lista, n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha todos os numeros da lista original maiores que n
    lista de inteiro, int -> lista'''
    if n in lista:
        return lista[n+1:]
    else:
        listaNova = lista + [n]
        list.sort(listaNova)
        if listaNova[-1] <= n:
            return []
        else:
            x = list.index(listaNova, n)
            return listaNova[x+1:]