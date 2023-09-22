def melhor_volta(matriz):
    resultados=[]
    for participante in range(6):
        melhor_t=min(matriz[participante])
        melhor_volta=list.index(matriz[participante],melhor_t)+1
        corredor=participante+1
        list.append(resultados,(corredor,melhor_t,melhor_volta))
    for i in range(1,6):
        for compara in resultados:
            if compara[i-1][1]<compara[i][1]:
                melhor=compara[i]
            else:
                melhor=compara[i+1]

    return resultados