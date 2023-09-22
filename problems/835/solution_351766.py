def melhor_volta(matriz):
    placar = []
    for i in matriz:
        list.append(placar, min(i))
        corredor = list.index(placar,min(placar))
    volta = list.index(matriz[corredor], min(placar))
    tupla = (corredor, min(placar), volta)
    return tupla