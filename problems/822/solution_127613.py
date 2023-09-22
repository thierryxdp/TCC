def repetidos(numeros):
    i=0
    repetido=0
    while i<len(numeros):
        if numeros[i]==numeros[i-1]:
            repetidos= repetidos +1
        i=i+1
    return repetidos