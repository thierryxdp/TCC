def acima_da_media(lista):
    '''Função que retorna as notas que ficaram acima da média.
    list->list'''
    
    list.sort(sum(lista))
    del lista[:8]
    return lista