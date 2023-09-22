def media_matriz(matriz):
    j = 0
    soma = 0 
    elementos = 0
    for i in matriz[j]:
        c = sum(matriz[j])
        soma = soma + c
        j = j + 1
        elementos = elementos + len(matriz[j])
    return soma/elementos