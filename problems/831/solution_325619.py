def lingua_p(pal):
    palavra=list(pal)
    p=palavra[:]
    for n in range(len(p)):
        if p[n] in 'aeiou':
            list.insert(palavra,n+1,'p')
            list.insert(palavra,n+2,p[n])
    return str.join('',palavra)