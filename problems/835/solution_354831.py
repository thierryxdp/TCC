def melhor_volta(matriz):
    ''' funcao que recebe uma matriz 6x10 com tempos de voltas em uma pista de corrida e retorna a melhor volta e o competidor que obteve a melhor volta. list --> tup'''
    menores_tempos = []
    melhores_voltas = []
    for competidores in matriz:
        menores_tempos.append(min(competidores))
        melhores_voltas.append(competidores.index(min(competidores))+1)
  
    
    
    
    campeao = menores_tempos.index(min(menores_tempos))+1
    melhor_tmp =min(menores_tempos)
    volta = melhores_voltas[campeao-1]
    
            
   
    return campeao,melhor_tmp,volta