def lingua_p(palavra):
    lista = list(range(0,len(palavra)))
    sep = list(palavra)
    for c in lista:
        if palavra[c] in 'AEIOUaeiou':
            list.insert(sep,c+1,'p' + palavra[c])
    ''.join(sep)
    return sep