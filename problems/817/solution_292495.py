def acima_da_media(lista_media):
    """Recebe uma lista de notas dos alunos e restorna uma lisca com as notas acima da media.
       list-> list

       Parameters:
       lista_media: Uma lista com as notas dos alunos."""
    x=len(lista_media)
    y=(sum(lista_media))/x
    list.append(lista_media,y)
    list.sort(lista_media)
    posicao=list.index(lista_media,y)+1
    if list.count(lista_media,int(y))>1:
        return lista_media[posicao+1:]
    else:
        return lista_media[posicao:]