def acima_da_media(nota):
    list.sort(nota)
    soma=sum(nota)
    ocorr=len(nota)
    media=(soma//ocorr)
    list.append(nota,media)
    list.sort(nota)
    p=list.index(nota, media)
    return nota[p+1:]