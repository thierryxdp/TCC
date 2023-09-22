def faltante(lista):
    '''Descobre o número faltante dentro da lista
    list->int'''
    list.sort(lista)
    i=0
     
    while i<len(lista):
        if not i==lista[i]:
            return i
        i=i+1