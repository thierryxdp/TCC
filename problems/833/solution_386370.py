def conta_numero(numero,matriz):
    soma = 0
    for i in len(matriz):
        for j in len(matriz[i]):
            if j == numero:
                soma = soma + 1 
    return soma