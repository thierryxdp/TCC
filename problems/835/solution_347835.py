def melhor_volta(matriz):
    for i in range(1,6):
        tempo1=min(matriz[i])
        for j in range(1,10):
            tempo2=min(matriz[j])
            if tempo1==tempo2:
                return tempo1
            	melhor_volta=tempo[j]
            	volta=tempo[i]
    return (tempo1,melhor_volta,volta)