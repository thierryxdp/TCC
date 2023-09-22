def melhor_volta(matriz):
    """Recebe como entrada uma matriz contendo as informações dos tempos,
    em segundos, dos corredores em cada volta e retorna uma tupla informando
    de quem foi a melhor volta, com qual tempo e em qual volta;list->tuple"""
    tmin=[]
    volta=[]
    for i in range(len(matriz)):
        tempos=[]
        for j in range(len(matriz[i])):
            list.append(tempos,matriz[i][j])
        list.append(tmin,min(tempos))
        for k in range(len(tempos)):
            if tempos[k]==min(tempos):
                list.append(volta,tempos[k]+1)
    for u in range(len(tmin)):
        if tmin[u]==min(tmin):
            corredor=u+1
            volta=u
    return (corredor,min(tmin),volta)