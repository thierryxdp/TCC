def acima_da_media(nota):
    list.sort(nota)
    list.del(nota,0)
    soma=sum(nota)
    ocorr=len(nota)
    i=(soma//ocorr)
    p=list.index(nota,i)
    return nota[p+1:]