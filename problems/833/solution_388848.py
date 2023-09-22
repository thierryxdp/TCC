def conta_numero(numero,matriz):
    vezes=0
    for linha in matriz:
        vezes=vezes+list.count(linha,numero)
    return vezes