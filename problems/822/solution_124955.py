def repetidos(lista):
    ''''''
    i = 0
    quant = 0
    while i < len(lista):
        
        if lista[i] == lista[i-1]:
            quant += 1
        i = i + 1
    return quant