def media_matriz(matriz):
    soma=0
    contador=0
    linha=0
    while linha < len(matriz):
		elemento=0
        while elemento < len(matriz[linha]):
            soma = soma + matriz[elemento]
            contador+=1
            elemento+=1
        linha +=1
    return round(soma/contador,2)