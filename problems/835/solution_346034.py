def melhor_volta(estatisticas):
    minimo=[]
    local=[]
    for i in range(len(estatisticas)):
        list.append(minimo,min(estatisticas[i]))
        for j in range(len(estatisticas[i])):
                if min(minimo) == estatisticas[i][j]:
                    local=local+list.index(estatisticas[i],min(minimo))                                        
    return ((list.index(minimo,min(minimo))+1),min(minimo),local)