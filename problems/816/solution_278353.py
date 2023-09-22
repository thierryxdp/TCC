def maiores(lista_inteiros, n):
    '''funcao que dada uma lista de numeros inteiros e um numero n, retorna outra lista que contem todos os
       numeros da lista original maiores que n
       list, int -> list'''
    maiores = []
    list.append(lista_inteiros, n)
    list.sort(lista_inteiros)
    indice = list.index(lista_inteiros, n)
    return lista_inteiros[indice:]