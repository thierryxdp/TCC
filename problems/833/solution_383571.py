def conta_numero(numero, matriz):
    soma = 0
    for i in matriz:     
        for c in i:
            if c == numero:
                soma = soma + 1
    return soma