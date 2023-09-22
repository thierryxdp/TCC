def co(numero,matriz):
    tamanho = len(matriz)
    x = 0
    for i in range(tamanho):
        linha = len(matriz[i])
        for j in range (linha):
            contador = 0
            n = matriz[i][j]
            if (numero == n):
                contador += 1
            x +=contador
    return x