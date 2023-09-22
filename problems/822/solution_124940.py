def repetidos(lista):
    ''''''
    i = 0
    quant = ''
    while i < len(lista):
        if lista[i+1] == lista[i]:
            quant += 1
        i = i + 1
    return quant