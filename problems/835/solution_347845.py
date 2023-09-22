def melhor_volta(matriz):
    melhores=[]
    for i in range(len(matriz[i])):
        menortempo=min(matriz[i])
        	melhores+=[menortempo,i+1]
    for j in range(len(melhores)):
        melhores[j][0]