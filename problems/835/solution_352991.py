def melhor_volta(matriz):
    """A função retorna uma tuppla contendo o dono da melhor volta, qual o tempo e em que rodada.
    list-->tuple"""
    tempos = []
    for list in matriz:
        tempos.append(min(list))
    menor = min(tempos)
    melhor = tempos.index(menor)
    todos = matriz[melhor]
    volta = todos.index(menor)

    return  melhor + 1, menor, volta +1