def melhor_volta(matriz):
    """Retorna em ordem: o corredor que fez a melhor volta, o tempo da melhor volta (em segundos) e a ordem da volta.
    Entrada: list(list)
    Saída: tuple
    """
    melhores = []
    for i in range(len(matriz)):
            list.append(melhores, min(matriz[i]))
    a = list.index(melhores, min(melhores)) + 1
    b = min(melhores)
    c = matriz [a][b]
    return a, b, c