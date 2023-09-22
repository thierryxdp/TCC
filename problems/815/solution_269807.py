def insere(lista_numero,n):
    '''retorna uma lista ordenada com um elemento adicionado e 
    em ordem crescente.
    lista, int -> lista'''
    
    nova_lista = lista_numero.append(n)
    return list.sort(nova_lista)