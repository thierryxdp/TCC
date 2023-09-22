def lingua_p(pal):
    palavra=list(pal)
    seq=list(range(palavra))
    for n in range(len(palavra)):
        if palavra[n] in 'aeiou':
            list.insert(palavra,n+1,'p'+palavra[n])
            list.append(seq,len(palavra))
    return str.join('',palavra)