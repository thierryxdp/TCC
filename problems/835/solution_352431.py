def melhor_volta(matriz):
    tempo=[]
    corredor=0
    volta=0
    for i in matriz:
        corredor+=1
        volta+=1
        tempo+=[[min(i),corredor,volta]]
    tempo=(tempo)
    return (tempo)