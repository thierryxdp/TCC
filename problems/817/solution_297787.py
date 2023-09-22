def acima_da_media(lista):
    
    media_turma = sum(lista)/len(lista)
    
    if media_turma in lista:
        list.sort(lista)
        indice = list.index(lista,media_turma)
        del lista[0:indice+1]
        
        return lista
        
    else:
        list.append(lista,media_turma)
        list.sort(lista)
        indice = list.index(lista,media_turma)
        del lista[0:indice+1]
        
        return lista