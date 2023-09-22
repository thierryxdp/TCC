def melhor_volta(m):
    '''Recebe como entrada uma matriz 6x10 com os tempos em segunds dos corredores de cada volta e retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta'''
    t=[]
    v=[]
    for i in range(len(m)):
        tempo=min(m[i])
        volta=list.index(m[i],tempo)+1
        list.append(t,tempo)
        list.append(v,volta)
    melhor_tempo=min(t)
    melhor_volta=v[list.index(t,min(t))]
    corredor=list.index(t,min(t))+1
    return(corredor,melhor_tempo,melhor_volta)