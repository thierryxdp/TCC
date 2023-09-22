def lingua_p(pal):
    palavra=list(pal)
    for n in range(len(palavra)):
        if palavra[n] in 'aeiou':
            list.insert(palavra,[n:(n+1)],'p')
            list.insert(palavra,[(n+1):(n+2)],palavra[n])
    return str.join('',palavra)