def conta_numero(numero, matriz):
    contagem = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                contagem += 1
    return contagem