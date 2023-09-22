def acima_da_media(nota):
    list.sort(nota)
    soma=sum(nota)
    ocorr=len(nota)
    i=(soma//ocorr)
    p=list.index(nota,i+1)
    return nota[p+1:]