def media_matriz(matriz):
    soma=0
    contador=0
    while linha < len(matriz):
        for elemento in matriz:
            soma = soma + elemento
            contador+=1
        linha +=1
    return round(soma/contador,2)