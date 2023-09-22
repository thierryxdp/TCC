def repetidos(numeros):
    i=0
    repetido=0
    while i<len(numeros):
        if numeros[i]==numeros[i-1]:
            repetidos= 1+ repetidos
        i=i+1
    return repetidos