def melhor_volta(matriz):
    """Retorna de quem foi a melhor volta, o tempo de volta e em qual volta foi atingido o menor tempo;
    list -> tuple
    """

    linhas = len(matriz)
    colunas = len(matriz[0])
    
    
    for i in range(linhas):
        for j in range(colunas):
            volta_rapida = min(matriz[i])
            piloto = list.index(matriz[i],volta_rapida)+1
            volta = list.index(matriz[i],volta_rapida)+1
    return (piloto, volta_rapida, volta)