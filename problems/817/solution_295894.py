def acima_da_media(lista):
    ''' dada uma lista com notas de alunos, retorna uma 
        lista ordenada com as notas acima da media.
        list-->list'''
    media_lista = sum(lista)/len(lista)
    indice_media_lista = list.index(lista,media_lista)
    list.sort(lista) = lista
    return lista[indice_media+1:]