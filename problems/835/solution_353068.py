def melhor_volta(m):

    corredor=0
    tempo=0
    volta=0
    lista=[]

    for i in range(0,6):
        lista.append(min(m[i]))
        for j in range(0,10):
            if m[i]==min(lista):
                corredor==i+1
                tempo==m[i]
                volta==j+1
                
    return corredor