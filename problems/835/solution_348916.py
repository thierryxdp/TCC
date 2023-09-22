def melhor_volta(matriz):
    '''Função que recebe como uma entrada uma matriz 6x10 com os tempos
    em segundos dos corredores em cada volta e deve retornar uma tupla
    informando: De quem foi a melhor volta da prova, com qual tempo e 
    em que volta.
    list -> tuple'''
    
    tempos = []
    corredor_e_volta = []
    
    for corredor in matriz:
        for volta in corredor:
            list.append(tempos, volta)
            list.append(corredor_e_volta, (corredor, volta))
            
    menor_tempo = min(tempos)
    a = list.index(tempos, menor_tempo)
    
    
    return (corredor_e_volta[a][0]+1, menor_tempo, corredor_e_volta[a][1]+1)