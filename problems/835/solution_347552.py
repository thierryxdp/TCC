def melhor_volta(matriz):
    
    mC = 10
    mT = 10
    mV = 10
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            
            if matriz[i][j] < mT:
                mC = i
                mT = matriz[i][j]
                mV = j
    return (mC,mT,mV)