def repetidos(numeros):
    contador=0
    soma=0
    while contador<len(numeros)-1:
        if numeros[contador+1]== numeros[contador]:
            soma+=1
        contador+=1
    return soma