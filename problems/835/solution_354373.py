def melhor_volta(matriz):
    ''' função que dada uma matriz com os tempos dos corredores
    em cada volta, retorna uma tupla informando de quem foi 
    a melhor volta da prova, com qual tempo e em que volta;
    matriz-> tupla'''
    qual_tempo=10
    qual_volta=10
    vencedor=10
    for v in range(0,len(matriz)):
        for t in range(0,len(matriz[v])):
            if min(matriz[v][t],qual_tempo)== matriz[v][t]:
                qual_tempo=min(matriz[v][t],qual_tempo)
                vencedor=v+1
                qual_volta=t+1
    return vencedor,qual_tempo,qual_volta