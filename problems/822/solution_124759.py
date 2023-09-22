def repetidos(numeros):
    contador=1
    soma=0
    while contador<len(numeros):
        if numeros[contador]== numeros[contador-1]:
            soma+=1
        contador+=1
    return soma