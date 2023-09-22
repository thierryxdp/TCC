def melhor_volta(matriz):
    """Funcao que recebe como entrada uma matriz 6X10 com os tempos
    em segundos dos corredores em cada volta.
    Entrada: list, list 
    Saída: float
    """
    corredores = []
    voltas = []
    tempos = []
    for i in matriz:
        for j in i:
            list.append(tempos,j)
            list.append(voltas, list.index(i,j))
            list.append(corredores, i)
    melhor_tempo = min(tempos)
    index = list.index(tempos,min(tempos))
    melhor_corredor = corredores[index] + 1 
    melhor_volta = voltas[index] + 1     
    return melhor_corredor,melhor_tempo,melhor_volta