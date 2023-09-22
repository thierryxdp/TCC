def melhor_volta(m):
    '''Retorna de quem foi a melhor volta da prova com qual tempo e em que volta,
       dada a matriz m 6 x 10 de entrada com os tempos de cada uma das 10 voltas
       dos 6 corredores;
       list -> tuple'''
    melhorCorredor=0
    melhorVolta=0
    melhorTempo=100000000
    for corredor in range(len(m)):
        for volta in range(len(m[0])):
            if m[corredor][volta]<melhorTempo:
                melhorCorredor=corredor
                melhorVolta=volta
                melhorTempo=m[corredor][volta]
    return (melhorCorredor+1,melhorTempo,melhorVolta+1)