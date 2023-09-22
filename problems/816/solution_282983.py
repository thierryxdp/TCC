def maiores(lista,n):
    """ Dada uma lista e um número inteiro "n" retorna uma lista com todos os elementos
    da lista original maiores que n.
    lista, int/float -> lista"""
    lista = lista+[n]
    list.sort(lista)
    indice=list.index(lista,n)
    sublista=lista[indice+1:]
    rep = list.count(sublista,n)
    if repeticoes != 0:
        sublista = sublista[repeticoes: ]
    return sublista