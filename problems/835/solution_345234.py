def melhor_volta(t):
    '''com base em uma matriz t 6x10 que contém os tempos em segundos dos
    corredores em cada volta, retorna uma tupla contendo quem fez a melhor
    volta, qual o seu tempo e em qual volta;
    list(list) -> tuple'''
    tempos = []
    voltas = []
    for i in t:
        x = min(i)
        y = list.index(i,x) + 1
        list.append(tempos,x)
        list.append(voltas,y)
    tempo = min(tempos)
    corredor = list.index(tempos,tempo) + 1
    volta = voltas[corredor-1]
    return corredor, tempo, volta