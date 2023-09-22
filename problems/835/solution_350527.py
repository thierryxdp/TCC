def melhor_volta(corrida):
    '''funcao que, dada uma matriz 6 x 10 contendo os tempos dos corredores, 
    retorna o corredor qe completou a prova em menor tempo, com seus respectivos tempo e volta.
    matriz -> tupla(int)'''
    tempos = []
    for corredor in range(len(corrida)):
        for tempo in corrida[corredor]:
            list.append(tempos,tempo)
    melhortempo = min(tempos)
    for corredor in range(len(corrida)):
        for volta in range(len(corrida[corredor])):
            if corrida[corredor][volta] == melhortempo:
                return (corredor+1, melhortempo, volta+1)