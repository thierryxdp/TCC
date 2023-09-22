def melhor_volta(matriz):
    """Função quue recebe como entrada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta,
    Dado que a pista permite 10 voltas para cada segundo, o retorno é uma tupla com 
    quem foi a melhor volta, com qual tempo e em qual volta
    list -> tuple"""
    volta = 0
    tempo = 100000
    corredor = 0
    indice = 1
    for i in matriz:
        if min(i) < tempo:
            tempo = min(i)
            corredor = indice
            volta = i.index(tempo) + 1
        indice += 1
    return(corredor, tempo, volta)