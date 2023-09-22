def conta_numero(numero, matriz):
    soma = 0
    for i in matriz:
        soma = 0
        for c in i:
            if c == numero:
        soma = soma + 1
    return soma