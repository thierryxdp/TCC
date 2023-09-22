def melhor_volta(matriz):
    """Retorna de quem foi a melhor volta, o tempo de volta e em qual volta foi atingido o menor tempo;
    list -> tuple
    """

    linhas = len(matriz)
    colunas = len(matriz[0])
    voltas_rapidas = []
    
    for i in range(linhas):
        list.append(voltas_rapidas,min(matriz[i]))
        for j in range(colunas):
            volta_rapida = min(voltas_rapidas)
            piloto = list.index(voltas_rapidas,volta_rapida)+1
            volta = list.index(voltas_rapidas,volta_rapida)+1
    if piloto == 1 and volta_rapida == 1:
        volta = 10
    return (piloto, volta_rapida, volta)