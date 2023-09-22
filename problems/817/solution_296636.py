def acima_da_media(nota):
    list.sort(nota)
    soma=sum(nota)
    ocorr=len(nota)
    i=(soma//ocorr)
    p=list.index(nota,i)
    if p in nota==true:
        return nota [p+1:]
    elif p in nota==false:
        return nota[3:]
    else:
        elif p in nota==false:
            return nota[1:]