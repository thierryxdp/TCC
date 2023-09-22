def melhor_volta (matriz):
    '''Funcao que, dada uma matriz, retorna quem fez a melhor volta, em quanto tempo e em que volta.
    list->tupla'''
    
    corredores = (1,2,3,4,5,6)
    voltas = (1,2,3,4,5,6,7,8,9,10)
    listaCorredorTempo = []
    temposMin = []
    corredor = 1 
    
    for corredores in matriz:
        tempoMin = min(corredores)
        
        list.append(listaCorredorTempo, (corredor, list.index(corredores, tempoMin), tempoMin)
        list.append(temposMin, tempoMin)
        corredor += 1
  	
    tempoGanhador = min(temposMin)
    
    for i in listaCorredorTempo:
        if tempoGanhador in i:
           return(i[0], i[1], tempoGanhador)
                                         
        for voltas in matriz[1]:
            min(corredores)