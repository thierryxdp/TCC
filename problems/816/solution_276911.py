def maiores(lista, n):
    '''Dada uma lista de números inteiros e o número inteiro n, retorna outra lista contendo apenas os números
    maior que n da lista original.
    list, int -> list'''
    list.sort(lista)
    lista_reversa = lista[:]
    list.reverse(lista_reversa)
    if n in lista:
        posicao= len(lista) - list.index(lista_reversa, n)
        return lista[posicao:]
    else: 
        list.insert(lista, 0, n)
        list.sort(lista)
        posicao_de_n = list.index(lista, n)
    return lista[posicao_de_n+1:]