def melhor_volta(matriz):
    menorTempo = 0
    corredor = 0
    menorVolta = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if (menorTempo == 0 or matriz[linha][coluna] < menorTempo):
                menorTempo = matriz[linha][coluna]
                corredor = linha
                menorVolta = coluna

    return (corredor, menorTempo, menorVolta)