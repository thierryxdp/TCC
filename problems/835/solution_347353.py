def melhor_volta(matriz):
    '''list(list) - > tuple'''
    temporesMenores = []
    voltaMaisRapida = []

    for m in matriz:
        tempoMin = min(m)
        temporesMenores.append(tempoMin)
        volta = m.index(tempoMin)
        voltaMaisRapida.append(volta)

    tempoMenor = min(temporesMenores)
    posicao = temporesMenores.index(tempoMenor) 

    return posicao + 1, tempoMenor, voltaMaisRapida[posicao] + 1