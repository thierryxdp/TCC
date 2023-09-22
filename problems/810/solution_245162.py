def acima_da_media (nota):
    soma=sum(nota)
    ni=len(nota)
    media=(soma//ni)
    list.append(nota,media)
    list.sort(nota)
    list.reverse(nota)
    i=list.index(nota,media)
    lista=nota[0:i]
    list.sort(lista)
        return lista