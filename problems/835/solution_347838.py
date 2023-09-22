def melhor_volta(matriz):
    '''função  que dada uma matriz 6x10 retorna o menor tempo 
    junto com de quem foi a melhor volta e em que volta
    list->list'''
    for i in range(1,7):
        tempo1=min(matriz[i])
        for j in range(1,11):
            tempo2=min(matriz[j])
            if tempo1==tempo2:
                return tempo1
            	melhor_volta=tempo[j]
            	volta=tempo[i]
    return (tempo1,melhor_volta,volta)