def melhor_volta(matriz):
    contaVoltas = 0
    menorTempo= []
    for jogador in matriz:
        for tempo in jogador:
            menorTempo += [tempo]           
            contaVoltas+=1

    return menorTempo