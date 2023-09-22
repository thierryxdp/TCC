def melhor_volta(m):

    corredor=0
    tempo=0
    volta=0
    lista=[]

    for i in range(6):
        lista.append(min(m[i]))
        for j in range(10):
            if m[i][j]==min(lista):
                corredor==i+1
                tempo==m[i][j]
                volta==j+1
                
    return m