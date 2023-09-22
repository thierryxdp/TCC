def conta_numero(numero,matriz):
    soma=0
    for linha in matriz:
        soma+=linha.count(numero)
    return soma