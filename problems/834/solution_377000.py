def media_matriz(x):
    tamanho = len(x)
    soma = 0
    termos = 0
    somapt1 = 0
    for i in range(tamanho):
        linha = len(x[i])
        for j in range (linha):
            n = x[i][j]
            somapt1 += n
            termos += 1
    soma = (somapt1)/termos
    return round(soma,2)