def melhor_volta(matriz):
    melhor=[]
    for i in range(len(matriz)):
        list.append(melhor, min(matriz[i]))
    tempo=min(melhor)
    quem=list.index(melhor,tempo)
    volta=list.index(matriz[quem],tempo)
    return quem+1, tempo, volta+1