def conta_numero(numero, matriz):
    linha=0
    count=0
    while linha<=len(matriz):
        if numero in matriz(linha):
            count=count+1
        linha=linha+1
    return count