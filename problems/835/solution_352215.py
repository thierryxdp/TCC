def melhor_volta(matriz):

    melhor_volta = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if coluna < melhor_volta:
                melhor_volta = coluna
                corredor = linha
    
    return  corredor, melhor_volta