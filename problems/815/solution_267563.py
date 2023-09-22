def insere(lista):
    '''função que insere um número n em uma lista lista_numero na sua posição ordenada dentro da mesma; list, int -> list'''
    
    l1 = lista[0]
    l2 = lista[1]
    lista_ordenada = list.append(l1, l2)
    
    return list.sort(lista_ordenada)