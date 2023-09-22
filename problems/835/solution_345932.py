def melhor_volta(matriz):
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            tempo=min(matriz[i])
            if resultado>tempo:
                resultado=tempo
                corredor=i
                coluna=list.index(matriz[i],tempo)