def insere(lista_numero,n):
    '''função que insere um número a uma lista e a coloca em ordem
    crescente.
    lista, int -> lista'''
    
    nova_lista = list.append(lista_numero,n)
    
    return list.sort(nova_lista)