def lingua_p(pal):
    palavra=list(pal)
    for n in range(palavra):
        if palavra[n] in 'aeiou':
            list.insert(palavra,(n-1),'p')
            list.insert(palavra,(n+1),'p')
    return str.join(palavra)