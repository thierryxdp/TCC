def melhor_volta(matriz):
    contaVoltas = 0
    tempo= []
    for jogador in matriz:
        for t in jogador:
            tempo += [t]           
            contaVoltas+=1
    	menorTempo = min(tempo)        

    return tempo