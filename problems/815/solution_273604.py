def insere(lista_numero,n):
    '''Retorna n dentro da lista de maneira que a lista continue 
    ordenada; list,int->list'''
    lista2= list.extend(lista_numero,n)
    lista3= lista_numero+ lista2
    return list.sort(lista3)