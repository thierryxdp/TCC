def melhor_volta(matriz):
    placar = []
    for i in matriz:
        list.append(placar, min(i))
        corredor = list.index(placar,min(placar))+1
    volta = list.index(matriz[corredor], min(placar))+1
    tupla = (corredor, min(placar), volta)
    return tupla