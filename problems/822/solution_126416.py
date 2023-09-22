def repetidos(numeros):
    contador = 1
    r = 0
    while contador < len(numeros):
        if numeros[contador] == numeros[contador-1]:
            r = r + 1
           
    return r