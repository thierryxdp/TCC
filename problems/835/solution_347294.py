def melhor_volta(matriz):
    resultados=[]
    for participante in range(6):
        melhor_t=min(matriz[participante])
        melhor_volta=list.index(matriz[participante],melhor_t)+1
        corredor=participante+1
        list.append(resultados,(corredor,melhor_t,melhor_volta))
    for compara in resultados:
        for i in range(6):
            if compara[i][1]<compara[i+1][1]:
                melhor=compara[i]
            else:
                melhor=compara[i+1]

    return melhor