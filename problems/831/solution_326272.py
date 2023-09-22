def lingua_p(palavra):
    lista = []
    for x in range(0,len(palavra)):
        if palavra[x] not in 'AEIOUaeiou':
            lista.append(str(palavra[x]))
        if palavra[x] in 'AEIOUaeiou':
            lista.append(str(palavra[x]))
            lista.append('p')
            lista.append(str(palavra[x]))
    return str(lista)