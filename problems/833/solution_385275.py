def conta_numero(numero,matriz):
    """retorna o numero de vezes que o numero aparece na matriz
    int, list-> int"""
    qnt = 0
    for linha in matriz:
        qnt = qnt + list.count(linha,numero)
    return qnt