def acima_da_media(lista):
    '''Função que retorna as notas que ficaram acima da média.
    list->list'''
    
    list.sort(lista)
    z= list.index(lista,5)
    
    del lista[:z]
    
    return lista