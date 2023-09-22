def lingua_p(palavra):
    lista = []
    for x in range(0,len(palavra)):
        if palavra[x] not in 'AEIOUaeiou':
            lista.append(str(x))
        if palavra[x] in 'AEIOUaeiou':
            lista.append(str(x))
            lista.append('p')
            lista.append(str(x))
    return lista