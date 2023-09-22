def acima_da_media(lista):
    
    
    media_turma = sum(lista)/len(lista)
    list.append(lista,media_turma)
    list.sort(lista)
    indice_media = list.index(lista,media_turma)
    
    del lista[0:indice_media+1]
    
    return lista