def lingua_p(pal):
    palavra=list(pal)
    seq=list(range(len(palavra)))
    for n in seq:
        if n<len(palavra):
            if palavra[n] not in 'bcdfghjklmnpqrstvwxyz':
                list.insert(palavra,n+1,'p'+palavra[n])
                list.append(seq,len(palavra))
    return str.join('',palavra)