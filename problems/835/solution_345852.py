def melhor_volta(estatisticas):
    minimo=[]
    c=0
    for i in range(0,6):
        list.append(minimo,min(estatisticas[i]))
        if min(minimo) in estatisticas[i]:
            c=c+1
    return ((list.index(minimo,min(minimo))+1),min(minimo),)