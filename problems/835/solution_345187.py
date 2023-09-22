def melhor_volta(matriz):
    t=[]
    v=[]
    for i in range(len(matriz)):
        tempo=min(matriz[i])
        volta=list.index(matriz[i],tempo)+1
        list.append(t,tempo)
        list.append(v,volta)
    melhor_tempo=min(t)
    melhor_volta=v[list.index(t,min(t))]
    corredor=list.index(t,min(t)+1)
    return (corredor,melhor_tempo,melhor_volta)