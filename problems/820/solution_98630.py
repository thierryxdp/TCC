def posLetra(palavra, letra, ocorrencia):
    i = 0
    u = 0
    while i < len(palavra):
        if palavra[i] in letra:
            u = u + 1
            if palavra.count(letra) < ocorrencia:
                return -1
            if u == ocorrencia:
                return i
        i = i + 1