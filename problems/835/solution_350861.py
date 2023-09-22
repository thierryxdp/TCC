def melhor_volta(tempos):
    '''
    Função que retorna uma tupla com todas as informações do melhor tempo.
    list->tuple
    '''
    menores_tempos = [min(tempos[0]),min(tempos[1]),min(tempos[2]),min(tempos[3]),min(tempos[4]),min(tempos[5])]
    mais_rapido = 0
    volta_mais_rapida = 0
    for elem in range(0,len(tempos)):
            if min(tempos[elem]) == min(menores_tempos):
                mais_rapido = mais_rapido + (elem+1)
    for elem2 in range(0,len(tempos)):
        for elem3 in range(0,len(tempos[elem2])):
            if tempos[elem2][elem3] == min(menores_tempos):
                volta_mais_rapida = volta_mais_rapida + (elem3+1)
    return (mais_rapido,min(menores_tempos),volta_mais_rapida)