def conta_numero(numero,matriz):
    contagem = 0
    for linha in range(len(matriz)):
        contagem = contagem + list.count(matriz[linha],numero)
    return contagem