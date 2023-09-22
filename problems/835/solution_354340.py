def melhor_volta(matriz):
    '''Dado uma matriz 6x10, a função deve retornar uma
    tupla informando de quem foi a melhor volta da prova,
    com o tempo e a volta;
    list(list)->tuple'''
    
    tempos_menores=[]
    voltas_melhores=[]
    jogadores_melhores=[]
    for i in range(len(matriz)):
        list.append(tempos_menores, min(matriz[i]))
        list.append(voltas_melhores, list.index(matriz[i],min(matriz[i])))
        list.append(jogadores_melhores,i)
    
    tempo_menor=min(tempos_menores)
    melhor_volta=voltas_melhores[list.index(tempos_menores,tempo_menor)]
    melhor_jogador=jogadores_melhores[list.index(tempos_menores,tempo_menor)]
    
    return(melhor_jogador,tempo_menor,melhor_volta)