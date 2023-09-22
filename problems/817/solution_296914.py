def acima_da_media(nota):
    list.sort(nota)
    soma=sum(nota)
    ocorr=len(nota)
    i=(soma//ocorr)
    p=list.index(nota,i)
    list.append(nota,p)
    lis.sort(nota)
    return nota[p+1:]