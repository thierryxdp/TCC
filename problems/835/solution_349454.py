def melhor_volta(matriz):
    """Retorna o corredor, o menor tempo e a volta;
    list -> tuple"""
    corredor = 0
    volta = 0
    menores_tempos= []
    for i in range(6):
        list.append(menores_tempos,min(matriz[i]))
    menor_tempo= min(menores_tempos)
    
    for i in range(6):
        if menor_tempo in matriz[i]:
            corredor = i + 1
    volta = list.index(matriz[corredor-1],menor_tempo) +1
    return (menor_tempo, corredor, volta)