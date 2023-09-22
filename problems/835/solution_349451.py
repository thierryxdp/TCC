def melhor_volta(matriz):
    """Retorna o corredor, o menor tempo e a volta;
    list -> tuple"""
    n_linhas = len(matriz)
    corredor = 0
    volta = 0
    menores_tempos= []
    for i in range(n_linhas):
        list.append(menores_tempos,min(matriz[i]))
    menor_tempo= min(menores_tempos)
    
    for i in range(n_linhas):
        if menor_tempo in matriz[i]:
            corredor = i + 1
    for j in range(10):
        if in matriz[corredor-1][j]:
            volta = j
    return (menor_tempo, corredor, volta)