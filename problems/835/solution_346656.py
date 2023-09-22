import math
def melhor_volta (matriz):
    '''Funcao que, dada uma matriz, retorna quem fez a melhor volta, em quanto tempo e em que volta.
    list->tupla'''
    

    listaCorredorTempo = []
    ganhou = []
    temposMin = []
    corredor = 1 
    
    tempoGanhador = math.inf
    for corredores in matriz:
        tempoMin = min(corredores)
        if tempoMin < tempoGanhador:
            tempoGanhador = tempoMin
        list.append(ganhou, (corredor, tempoGanhador, list.index(corredores, tempoMin)+1))
        
        corredor += 1
    
    return (i[0], tempoGanhador, i[1])