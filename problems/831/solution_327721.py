def lingua_p(w):
    '''Recebe uma palavra e Retorna essa mesma palavra traduzida para a
    lingua P como descrito ao lado;
    str -> str'''
    x=str.lower(w)
    l=list(x)
    c=0
    for i in l:
        if i in 'aeiouáéíóúãõâêîôû':
            list.insert(l,c,('p'+i))
        c=c+1
    return str.join('',l)