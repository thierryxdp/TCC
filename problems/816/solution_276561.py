def maiores(lista, n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha todos os numeros da lista original maiores que n
    lista de inteiro, int -> lista'''
    list.sort(lista)
    lista_nova = [lista] + [n]
    list.sort(lista_nova)
    list.split(lista_nova, ",")
    x = list.index(lista_nova, n)
    lista_nova = lista_nova[x+1:]
    " ".join(lista_nova)
    return lista_nova