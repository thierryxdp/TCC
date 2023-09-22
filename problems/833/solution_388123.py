def conta_numero(numero,matriz):
    """
    função que conta e retorna quantas vezes numero
    aparece na matriz
    """
    quantidade = 0
    for linha in matriz:
        quantidade = quantidade +list.count(linha,numero)
        return quantidade