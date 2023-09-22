def repetidos (numeros):
    indice = 1
    repetidos = 0 
    while indice < len(numeros):
        if numeros[indice] == numeros [indice - 1]:
            repetidos = repetidos + 1
        indice = indice + 1
        if len (numeros) == 2 and numeros [0] == numeros [1]:
            repetidos = 1
    return repetidos