def insere (lista_numero,n):
    '''Recebe uma lista ordenada crescente e um número n e entrega uma 
    nova lista com o n colocado na sua posição correta (list->list)'''
    lista_com_n = list.append(lista_numero,n)
    lista_nova = list.sort(lista_com_n)
    return lista_nova