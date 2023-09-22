def lingua_p(palavra):
    lista = list(range(0,len(palavra)))
    sep = list(palavra)
    for c in lista:
        if palavra[c] in 'AEIOUaeiouéóúáí':
            list.insert(sep,c+3,'p' + palavra[c])
    a = ''.join(sep)
    return a