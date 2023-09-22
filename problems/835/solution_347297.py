def melhor_volta(matriz):
    resultados=[]
    for participante in range(6):
        melhor_t=min(matriz[participante])
        melhor_volta=list.index(matriz[participante],melhor_t)+1
        corredor=participante+1
        list.append(resultados,(corredor,melhor_t,melhor_volta))
        for compara in resultados:
            for i in range(6):
                dado1=compara[i][1]
                dado2=compara[i+1][1]
                if dado1<dado2:
                    melhor=dado1
                else:
                    melhor=dado2

    return melhor