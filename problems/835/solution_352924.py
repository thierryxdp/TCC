def melhor_volta(m):

    corredor=''
    tempo=''
    volta=''
    
    for i in range(0,6):
        for j in range(0,10):
            if m[i][j] in min(m):
                corredor==i
                tempo==m[i][j]
                volta==j+1
                

    return (corredor,tempo,volta)