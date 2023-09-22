def conta_numero(numero, matriz):
    """Funcao que retorna quantas vezes um certo numero aparece na matriz.
    int, list(list) - > int"""
    qtd = 0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                qtd += 1
    return qtd