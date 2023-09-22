def melhor_volta(matriz):
    ''' funcao que recebe uma matriz 6x10 com tempos de voltas em uma pista de corrida e retorna a melhor volta e o competidor que obteve a melhor volta. list --> tup'''
    menores_tempos = []
    melhores_voltas = []
    for competidores in matriz:
        menores_tempos.append(min(competidores))
        for tempos in competidores:
            melhores_voltas.append(tempos.index(min(tempos))
            
   
    return (menores_tempos.index(min(menores_tempos))+1,min(menores_tempos),(melhores voltas.index(min(melhores_voltas))+1)