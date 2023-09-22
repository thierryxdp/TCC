def acima_da_media(nota):
    list.sort(nota)
    soma=list.sum(nota)
    ocorr=len(nota)
    i=(soma/ocorr)
    return list.index(nota,i)