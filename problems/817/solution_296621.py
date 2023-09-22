def acima_da_media(nota):
    list.sort(nota)
    soma=sum(nota)
    ocorr=len(nota)
    i=(soma//ocorr)
    if p=list.index(nota,i):
        return nota[p+1:]
    else:
        return