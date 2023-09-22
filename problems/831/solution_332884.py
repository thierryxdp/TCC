def lingua_p(p):
    
    lista = list(p)
    ls = []
    for x in p:
        ls.append(x)
        if x in 'aeiou':
            ls.append('p')
            ls.append(x)
    return ''.join(ls)