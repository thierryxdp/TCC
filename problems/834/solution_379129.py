def media_matriz(matriz):
    ''''''
    soma=0
    quantidade=0
    
    for numero in matriz:
        soma = soma + sum(numero)
        quantidade = quantidade + len(numero)
    return round(soma/quantidade,2)