def melhor_volta(m):

    corredor=0
    tempo=0
    volta=0
    lista=min(m)
    
    for i in range(0,6):
        for j in range(0,10):
            if m[i][j]==min(lista):
                corredor==i+1
                tempo==m[i][j]
                volta==j+1
                
                
    return lista