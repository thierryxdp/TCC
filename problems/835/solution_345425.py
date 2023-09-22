def melhor_volta(matriz):
    """Retorna de quem foi a melhor volta, o tempo de volta e em qual volta foi atingido o menor tempo;
    list -> tuple
    """

    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for i in range(linhas):
        for j in range(colunas):
            volta_rapida = min(matriz[i])
            pos = list.index(matriz,matriz[i])
            volta = list.index(matriz,matriz[i])
    return pos, volta_rapida, volta