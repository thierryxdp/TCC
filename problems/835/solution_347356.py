def melhor_volta (matriz_voltas):
    """Recebe uma matriz com informações dos tempos das 
    voltas de 6 corredores, cada um com 10 voltas, e retorna
    de quem foi o menor tempo da volta, o tempo dessa volta
    e qual volta ela foi.
    list -> tuple"""
    melhor_corredor = 1
    melhor_volta = 1
    tempo_volta = []
    for voltas in matriz_voltas:
        if voltas == min(matriz_voltas):
            melhor_corredor += list.index(matriz_voltas, voltas)
        for volta in voltas:
            if volta == min(voltas):
                melhor_volta += list.index(voltas, volta)
                list.append(tempo_volta, volta)
    return (melhor_corredor, tempo_volta, melhor_volta)