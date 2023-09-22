def melhor_volta(m):

    corredor=0
    tempo=0
    volta=0

    for i in range(0,6):
        lista=[]
        for j in range(0,10):
            lista.append(min(m[i]))
            if m[i][j]==min(m):
                corredor==i+1
                tempo==m[i][j]
                volta==j+1
                
    return (corredor,tempo,volta)