def acima_da_media(lista):
    '''Função que retorna as notas que ficaram acima da média.
    list->list'''
    
    list.sort(lista)
    z= list.index(lista,5)
    y= list.index(lista,x<5)
    if 5 in lista:
        del lista[:z]
        return lista
    else:
        del lista[:y]
        return lista