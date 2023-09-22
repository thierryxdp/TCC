import math
def melhor_volta (M):   
    listaCorredorTempo = []
    ganhou = []
    temposminimo = []
    corredor = 1    
    tempoGanhador = math.inf
    for corredores in M:
        temposminimo = min(corredores)
        if temposminimo < tempoGanhador:
            tempoGanhador = temposminimo
            list.append(ganhou, (corredor, tempoGanhador, list.index(corredores, temposminimo)+1))
        corredor += 1        
    return ganhou[-1]