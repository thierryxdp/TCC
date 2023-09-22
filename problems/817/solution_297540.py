def acima_da_media(nota):
    soma=sum(nota)
    Ni=len(nota)
    media=(soma//Ni)
    list.append(nota,media)
    list.max(nota)
    i=list.index(nota,media)
    lista=nota[0:i]
    list.sort(lista)
    return lista