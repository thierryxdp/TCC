def insere(lista_numero,n):
    '''função que insere um número a uma lista e a coloca em ordem
    crescente.
    lista, int -> lista'''
    
    nova_lista = list.insert(lista_numero,n,0)
    
    return list.sort(nova_lista)