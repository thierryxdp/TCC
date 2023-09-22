def melhor_volta(matriz):
    volta=-1
    corredor=-1
    tempo=[]
    for i in matriz:
        corredor+=1
        tempo+=[min(i)]
        volta+=1
    tempo=min(tempo)        
    return (corredor,tempo,volta)