def maiores(lista, n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha todos os numeros da lista original maiores que n
    lista de inteiro, int -> lista'''
    list.sort(lista)
    lista2 = [lista] + [n]
    list.sort(lista2)
    list.split(lista2, ",")
    x = list.index(lista2, n)
    lista_nova = lista2[x+1:]
    " ".join(lista_nova)
    return lista_nova