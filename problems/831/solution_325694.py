def lingua_p(palavra):
    lista = list(range(0,len(palavra)))
    sep = list(palavra)
    a = 0
    for c in lista:
        if palavra[c] in 'AEIOUaeiouéóúáí':
            list.insert(sep,c+a,'p' + palavra[c])
            a = a + 1
    a = ''.join(sep)
    return a