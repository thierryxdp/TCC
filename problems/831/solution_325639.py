def lingua_p(pal):
    palavra=list(pal)
    tam=range(len(palavra))
    for n in tam:
        if palavra[n] not in 'bcdfghjklmnpqrstvwxyz':
            list.insert(palavra,n+1,'p'+palavra[n])
            tam=range(len(palavra))
    return str.join('',palavra)