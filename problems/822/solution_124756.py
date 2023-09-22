def repetidos(numeros):
    contador=0
    soma=0
    while contador<len(numeros):
        if numeros[contador+1]== numero[contador]:
            soma+=1
        contador+=1
    return soma