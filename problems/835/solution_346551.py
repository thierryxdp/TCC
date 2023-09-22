def melhor_volta(m):
    '''Dado uma matriz 6 (corredores) x10 (voltas), a funcao calcula:
    a melhor volta; o tempo dessa volta; em qual volta.
    list -> tuple(int,float,int)'''
    corredor=0
    tempo=[]
    volta=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            #para o tempo:
            tempo.append(m[i][j])
            menor_tempo=min(tempo)
            #para o melhor corredor:
            if menor_tempo in m[i]:
            	corredor=i+1
            #para a volta:
            volta=m[i].index(menor_tempo)+1
    return (corredor,menor_tempo,volta)