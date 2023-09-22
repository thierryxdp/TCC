def media_matriz(matriz):
    ''''''
    soma=0
    quantidade=0
    
    for num in matriz:
        soma = soma + sum(num)
        quantidade = quantidade + len(num)
    return round(soma/quantidade,2)