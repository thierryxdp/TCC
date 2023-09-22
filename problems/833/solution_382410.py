def conta_numero(numero,matriz):
    soma = 0
    x = 0
    for i in range(len(matriz)):
        soma = soma = 1
        for j in range(len(matriz[i])):
            if numero in j:
                soma = soma + 1
            else:
                continue
    return soma