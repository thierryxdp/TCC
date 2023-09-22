def melhor_volta(matriz):
    '''Retorna o corredor com a volta mais rápida assim como o tempo e a própria volta.
    list --> tuple'''
    
    melhCor = 0
    melhVol = 0
    melhTemp = matriz[0][0]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if melhTemp > matriz[i][j]:
                melhTemp = matriz[i][j]
                melhVol = j+1
                melhCor = i+1
                
	return (melhCor,melhTemp,melhVol)