def repetidos(lista):
    i = len(lista)-1
    numeros = []
    while i > 0:
        if [lista[i]] == [lista[i-1]]:
            numeros = numeros + [lista[i]]
        i = i - 1
    return len(numeros)