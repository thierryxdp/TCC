def conta_numero(numero,matriz):
    quant=0
    for linha in matriz:
        if numero in linha:
            quant+=1
    return quant