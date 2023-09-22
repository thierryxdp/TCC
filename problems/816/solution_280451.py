def maiores(lista,n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista
    com os mesmos componentes da lista original maiores que n
    lista, int -> lista'''
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    ind=list.index(lista,n)
    listaf=lista[ind+1:]
    return listaf