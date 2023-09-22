def maiores(lista,n):
    '''a função retornaoutra lista que contém todos numeros da lista original maiores que n'''
    
    litsa = lista+ [n]
    list.sort(lista)
    list.reverse(lista)
    
    Indice= list.index(x)
    nova_lista = lista[:Indice]
    
    list.reverse(nova_lista)
    return nova_lista