def maiores(lista,n):
    '''uma fun ̧c ̃ao maiores que, dada uma lista de n ́umeros inteiros e um n ́umero inteiro n, retorna outra
lista, que contenha todos os n ́umeros da lista original maiores que n; list,n->list'''
    
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    indice= list.index(lista,n)

    fatiado= lista[indice+1:]
    return fatiado