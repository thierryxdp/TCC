def melhor_volta(matriz):
    
    mC = 2
    mT = 2
    mV = 2
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < mT:
                mC = i
                mT = matriz[i][j]
                mV = j
    return (mC+1,mT,mV+1)