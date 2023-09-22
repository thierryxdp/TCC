def melhor_volta(estatisticas):
    """Essa função retorna de quem foia a melhor volta,com qual tempo e em que volta com base em uma matriz"""
    """list->tuple"""
    minimo=[]
    local=[]
    for i in range(len(estatisticas)):
        list.append(minimo,min(estatisticas[i]))
        for j in range(len(estatisticas[i])):
                if min(minimo) == estatisticas[i][j]:
                    local=local+[list.index(estatisticas[i],min(minimo))]                                       
    return ((list.index(minimo,min(minimo))+1),min(minimo),(local[-1]+1))