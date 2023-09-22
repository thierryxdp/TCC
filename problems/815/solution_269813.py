def insere(lista_numero,n):
    '''retorna uma lista ordenada com um elemento adicionado e 
    em ordem crescente.
    lista, int -> lista'''
    
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero