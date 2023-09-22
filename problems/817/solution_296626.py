def acima_da_media(nota):
    list.sort(nota)
    nulo=list.index(nota,0)
    list.del(nota,nulo)
    soma=sum(nota)
    ocorr=len(nota)
    i=(soma//ocorr)
    p=list.index(nota,i)
    return nota[p+1:]