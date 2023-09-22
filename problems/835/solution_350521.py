def melhor_volta(corrida):
    '''funcao que, dada uma matriz 6 x 10 contendo os tempos dos corredores, 
    retorna o corredor qe completou a prova em menor tempo, com seus respectivos tempo e volta.
    matriz -> tupla(int)'''
    tempos = []
    for corredor in range(len(corrida)):
        for tempo in corrida[corredor]:
            list.append(tempos,tempo)
    melhortempo = min(tempos)
    for corredor in range(1,len(corrida)+1):
        for volta in range(1,len(corrida[corredor])+1):
            if corrida[corredor][indice] == melhortempo:
                return (corredor, tempo, volta)