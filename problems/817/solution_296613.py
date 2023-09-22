def acima_da_media(nota):
    list.sort(nota)
    soma=sum(nota)
    ocorr=len(nota)
    i=(soma/ocorr)
    list.index(nota,i)
    return nota[i:]