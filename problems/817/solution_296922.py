def acima_da_media(nota):
    soma=sum(nota)
    Ni=len(nota) 
    media=(soma//Ni) 
    list.append(nota,media)
    list.sort(nota)
    list.reverse(nota)
    i=list.index(nota,media)
    lista=nota[0:i]
    return list.sort(lista)