def maiores(lista,n):
    '''a função retorna outra lista que contém todos numeros da lista original maiores que n'''
    
    lista= lista + [n]
    list.sort(lista)
    list.reverse(lista)
    
    Indice= list.index (lista,n)
    nova_lista = lista[:Indice]
    
    list.reverse(nova_lista)
    return nova_lista