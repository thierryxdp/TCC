def melhor_volta(matriz):
    melhorvoltadecada=[]
	for x in matriz:
        melhorvoltadecada.append((min(x),x.index(min(x))))
    melhortempo=min(melhorvoltadecada)[0]
    melhorvolta=min(melhorvoltadecada)[1]+1
    melhorcorredor=melhorvoltadecada.index(min(melhorvoltadecada))+1
    return (melhorcorredor,melhortempo,melhorvolta)