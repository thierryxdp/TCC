def lingua_p(pal):
    palavra=list(pal)
    p=
    for n in range(len(palavra)):
        if palavra[n] in 'aeiou':
            list.insert(palavra,n+1,'p'+palavra[n])
    return str.join('',palavra)