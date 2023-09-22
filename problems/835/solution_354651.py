def melhor_volta(matriz):
    jogador=1
    lista=[]
    volta=1 #volta
    q=min(matriz[0])
    w=min(matriz[1])
    e=min(matriz[2])
    r=min(matriz[3])
    t=min(matriz[4])
    y=min(matriz[5])
    listatempo=[q,w,e,r,t,y]
    menortempo=min(listatempo) #tempo
    for i in range(len(listatempo)):
        if listatempo[i]==menortempo:
            jogador+=i #jogador
            lista.append(matriz[i])
    for j in range(len(lista[0])):
        if lista[0][j]==menortempo:
            volta+=j
    return jogador, menortempo,volta