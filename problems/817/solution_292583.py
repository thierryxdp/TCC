def media(lista):
    
    """Funçao que recebe uma lista com notas de alunos e retorna outra com as
    notas dos alunos que ficaram acima da media"""
    
    media = sum(lista_notas)/len(lista_notas)
    list.append(lista_notas, media)
    list.sort(lista_notas)
    x = list.index(lista_notas, media)+1
    na_media = list.count(lista_notas, media)-1
    acima_media = lista_notas[(x+na_media):]
    if len(lista_notas) > 1:
        return (media, acima_media)
    else:
        return (media,[])