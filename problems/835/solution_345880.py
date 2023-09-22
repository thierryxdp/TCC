def melhor_volta(estatisticas):
    minimo=[]
    local=0
    for i in range(0,6):
        list.append(minimo,min(estatisticas[i]))
        if min(minimo) in estatisticas[i]:
            local=local+list.index(estatisticas[i],min(minimo))
    return ((list.index(minimo,min(minimo))+1),min(minimo),local)