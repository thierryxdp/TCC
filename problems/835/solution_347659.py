def melhor_volta(corrida):
    ''' funcao que recebe uma matriz 6x10 no parametro corrida e 
    retorna quem fez a melhor volta 
    list -> tupla'''
    tmin1= corrida[0][0]
    for corredor in range(len(corrida)):
        for volta in range(len(corrida[corredor])):
            if tmin1>corrida[corredor][volta]:
                tmin1= corrida[corredor][volta]
    for corredor in range(len(corrida)):
        for volta in range(len(corrida[corredor])):
            if tmin1==corrida[corredor][volta]:
                return corredor +1, tmin1, volta +1