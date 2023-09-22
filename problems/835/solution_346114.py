def melhor_volta(matriz):
    lista=[]
    for i in range(0,7):
        for matriz[i] in range(0,7):
            matriz1=list.sort(matriz[i])
            lista+=[matriz1[0]]
        i+=1
        return lista