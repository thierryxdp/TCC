def acima_da_media(lista):
    """recebe uma lista com as notas dos alunos e retorna outra lista ordenada com as notas que ficaram acima da média"""
    if int(media) in lista :
        media=sum(lista)/len(lista)
        list.append(lista,media)
        list.sort(lista)
        indice=list.index(lista,media)
        del lista[indice]
        return lista[int(indice)+1:]
        
    
    
else:
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    indice=list.index(lista,media)
    del lista[indice]
    return lista[int(indice):]