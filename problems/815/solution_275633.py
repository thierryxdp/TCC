def insere(lista_numero,n):
    '''dada uma lista ordenada, inclui o numero n de forma a manter a ordem na lista; list,int -> list'''
    nova_lista = lista_numero + [n,]
    list.sort(nova_lista)
    return nova_lista