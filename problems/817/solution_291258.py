def acima_da_media(lista_nota):
    media_das_notas=sum(lista_nota)/len(lista_nota)
    list.sort(media_das_notas)
    lista=list.range(media_das_notas,100)
    return media_das_notas