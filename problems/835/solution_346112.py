def melhor_volta(matriz):
    lista=[]
    for i in range(0,7):
        for matriz[i] in range(0,7):
            lista+=[min(matriz[i])]
        i+=1
        return lista