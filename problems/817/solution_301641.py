def acima_da_media(lista):
    '''função que dada uma lista com as notas
    retorna uma lista ordenada com as notas acima da média
    lista -> lista'''
    
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    z=len(lista)
    y=list.index(lista,media)
    return lista[y+1:z]