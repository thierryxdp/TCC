def insere(lista_numero,n):
    '''retorna uma lista ordenada com um elemento adicionado e 
    em ordem crescente.
    lista, int -> lista'''
    
    ordenada = list.sort(list.append(lista_numero,n))
    
    return ordenada