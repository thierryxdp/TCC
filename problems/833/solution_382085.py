def conta_numero(numero,matriz):
    """ dado um numero e uma matriz, conta e retorna quantas vezes o numero aparece na matriz"""
    contagem=0
    for linha in range(len(matriz)):
        contagem=contagem+ list.count(matriz[linha],numero)
    return contagem