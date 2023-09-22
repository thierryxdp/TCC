def lingua_p(pal):
    palavra=list(pal)
    for n in range(len(palavra)+1):
        if palavra[n] in 'aeiou':
            list.insert(palavra,n+1,'p'+palavra[n])
    return str.join('',palavra)