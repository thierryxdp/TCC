def lingua_p(palavra):
    s = ""
    lista = []
    for x in range (0, len(palavra)):
        if palavra[x] not in 'AEIOUaeiouáéíóú':
            lista.append(str(palavra[x]))
        if palavra[x] in 'AEIOUaeiouáéíóú':
            lista.append(str(palavra[x]))
            lista.append('p')
            lista.append(str(palavra[x]))
    return s.join(lista)