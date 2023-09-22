def melhor_volta(tempo):
    listagem=[0,float('inf'),0]
    for i in range(6):
        for j in range(10):
            if tempo[i][j]<listagem[1]:
                listagem=i+1,tempo[i][j],j+1
    return listagem