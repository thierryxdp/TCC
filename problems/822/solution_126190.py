def repetidos(lista):
    qtdRepetidos = 0
    i=1
    while i<len(lista):
        if lista[i-1] == lista[i]:
            qtdRepetidos += 1
        i=i+1
    return qtdRepetidos