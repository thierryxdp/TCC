def melhor_volta(matriz):
    ''' funcao que recebe uma matriz 6x10 com tempos de voltas em uma pista de corrida e retorna a melhor volta e o competidor que obteve a melhor volta. list --> tup'''
    menores_tempos = []
    melhores_voltas = []
    for competidores in matriz:
        menores_tempos.append(min(competidores))
    
    
    
    campeao = menores_tempos.index(min(menores_tempos))+1
    melhor_tmp =min(menores_tempos)
            
   
    return (competidores)