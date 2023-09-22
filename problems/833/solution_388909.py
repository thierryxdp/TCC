def conta_numero(numero, matriz):
    qtd = 0
    for linha in matriz:
        for j in linha:
            if numero == j:
                qtd = qtd + 1     
    return qtd