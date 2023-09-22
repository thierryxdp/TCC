def media(lista):
    
    """Funçao que recebe uma lista com notas de alunos e retorna outra com as
    notas dos alunos que ficaram acima da media"""
    
    media = sum(lista)/len(lista)
    list.append(lista, media)
    list.sort(lista)
    x = list.index(lista, media)+1
    na_media = list.count(lista, media)-1
    acima_media = lista[(x+na_media):]
    
    if len(lista) > 1:
        
        return (media, acima_media)
    
    else:
        
        return (media,[])