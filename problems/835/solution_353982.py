def melhor_volta(matriz):
    '''
    função que recebe como entrada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta;
    list(list) -> tuple
    '''
    volta_rap_pil = []
    for linha in matriz:
        volta_rap_pil = volta_rap_pil + [min(linha)]
        indice1 = list.index(matriz,volta_rap_pil)
        indice2 = list.index(matriz,linha) + 1
    volta_mais_rapida = min(volta_rap_pil)
    piloto = indice2 + 1
    volta = indice1 + 1
    return (piloto,volta_mais_rapida,volta)