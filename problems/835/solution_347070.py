def melhor_volta (matriz):
    """funçao que recebe uma matriz 6x10 e nela 6 corredores realizam 10 voltas e retorna o corredor com menor tempo e volta;
    entrada: list
    saida: tuple (int,int,int)"""
    menores = []
    for i in matriz:
        menores += [min (i)]
    melhor = min (menores)
    c = list.index (menores, melhor)
    v = list.index (matriz[c], melhor)
    return (c+1, melhor, v+1)