def conta_numero(n,matriz):
    qtde = 0
    for linha in matriz:
        for aij in linha:
            if aij == n:
                qtde = qtde + 1
    return qtde