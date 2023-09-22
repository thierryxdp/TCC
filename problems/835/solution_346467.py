def melhor_volta(m):
    """Recebe uma matriz 'm' 6x10 com os 10 tempos em segundos dos 6 corredores e retorna uma tupla informando de quem foi a melhor volta da prova,com qual tempo e em que volta;list->tuple"""
    corredores=[]
    for i in range(1,7):
        for j in range(1,11):
            corredor=list.index(m,min(m))+1
            volta=list.index(min(m[corredor]))+1
            tempo=min(m[corredor])
    return (corredor,tempo,volta)