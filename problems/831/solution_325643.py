def lingua_p(pal):
    palavra=list(pal)
    tam=list(range(len(palavra)))
    for n in tam:
        if palavra[n] in 'aeiouáéíóúàèìòùâêîôûãõ':
            list.insert(palavra,n+1,'p'+palavra[n])
            list.append(tam,len(palavra)-1)
    return str.join('',palavra)