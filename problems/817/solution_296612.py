def acima_da_media(nota):
    list.sort(nota)
    soma=sum(nota)
    ocorr=len(nota)
    i=(soma/ocorr)
    return list.index(nota,i)