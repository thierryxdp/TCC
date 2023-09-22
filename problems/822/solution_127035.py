def repetidos (lista0):
    '''função que dada uma lista retorna quantas vezes um elemento é igual ao elemento anterior;
    list->int'''
    i = 0
    lista1 = []
    while i<len(lista0):
        lista0[i]==lista0[i+1]
        lista1 = lista1 + [lista0[i],]
    i= i+1
    return lista1