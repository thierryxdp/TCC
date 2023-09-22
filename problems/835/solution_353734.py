def melhor_volta(mtx):

    minimo  = 10**15   
    
    for i in range(6):
        for j in range(10):
            if (mtx[i][j] < minimo):
                minimo = mtx[i][j]
                lin    = i
                col    = j
    
    return 'Corredor: '+str(lin+1)+';'+'Volta: '+str(col+1)+';'+'Tempo: '+str(minimo)