def conta_numero(numero,matriz):
    quantidade = 0
    for linha in matriz:
        quant = quantidade + list.count(linha,numero)
    return quantidade