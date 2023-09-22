def melhor_volta(m):

    corredor=0
    tempo=0
    volta=0
    
    for i in range(0,6):
        for j in range(0,10):
            if m[i][j] in min(m):
                lista==min(m)
                if m[i][j] in min(lista):
                    corredor==i
                    tempo==m[i][j]
                    volta==j+1
                

    return min(lista)