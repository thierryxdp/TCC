def insere(lista_numero,n):
    '''retorna uma lista ordenada com um elemento adicionado e 
    em ordem crescente.
    lista, int -> lista'''
    
    nova_lista = lista_numero[len(lista_numero):] = [n]
    ordenada = list.sort(nova_lista)
    return ordenada