def melhor_volta(m):

    corredor=0
    tempo=0
    volta=0
    lista=[]

    for i in range(0,6):
        for j in range(0,10):
            lista.append(min(m[i]))
            if m[i]==min(m[i]):
                corredor==i+1
                tempo==m[i][j]
                volta==j+1
                
    return lista