def melhor_volta(matriz6x10)
    for corredor in range(6):
        for volta in range(10):
            menor = min(matriz6x10[corredor][volta])
    return (corredor, menor, volta)