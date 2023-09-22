def conta_numero (numero: int, matriz: list) -> int:
    """Retorna quantas vezes o, inteiro, numero aparece em matriz."""
    contador = 0
    for linha_i in matriz:
        for coluna_j in linha_i:
            if coluna_j == numero:
                contador += 1
    return contador