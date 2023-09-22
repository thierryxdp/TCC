def melhor_volta(matriz):
    corredores = []
    tempos = []
    voltas = []
    for i in range(len(matriz)):
        corredor = 0
        tempo = 0
        volta = 0
        for j in range(len(matriz[0])):
                corredor += i
                tempo += matriz[i][j]
                volta += matriz[i].index(tempo)
        list.append(corredores,corredor)        
        list.append(tempos,corredor)
        list.append(voltas,volta)
    melhor = min(tempos)
    indice = tempos.index(min(tempos))
    quem = corredores[indice] +1
    volt = voltas[indice] +1
    return quem, melhor, volt