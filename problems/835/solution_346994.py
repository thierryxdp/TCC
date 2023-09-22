def melhor_volta(matriz):
    """A função recebe uma matriz 6x10 com os tempos dos corredores em
    cada volta, e retorna uma tupla informando de quem foi a melhor
    volta, com qual tempo e em que volta;
    list(list) -> tuple"""
    x = []
    y = []
    for i in matriz:
        list.append(x, min(i))
        k = list.index(i, min(i))
        list.append(y, k)
    menor_volta = min(x)
    melhor_corredor = x.index(menor_volta)+1
    melhor_volta = y[x.index(menor_volta)]+1
    return menor_volta, melhor_corredor, melhor_volta