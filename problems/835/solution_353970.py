def melhor_volta(matriz):
    '''
    função que recebe como entrada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta;
    list(list) -> tuple
    '''
    volta_rap = []
    for linha in matriz:
        volta_rap = volta_rap + [min(linha)]
    return volta_rap