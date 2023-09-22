def melhor_volta(matriz):
    voltas=[]

    #Crio uma lista com todas as voltas dos participantes em ordem
    
    for i in range(6):
        for j in range(10):
            voltas=voltas+[matriz[i][j]]

    menortempo=min(voltas)
    n=list.index(voltas,menortempo)+1

    if n%10!=0:
        corredor=(n//10)+1
        volta=n%10

    else:
        corredor=n//10
        volta=10

    return (corredor,menortempo,volta)