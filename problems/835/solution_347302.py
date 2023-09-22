def melhor_volta(matriz):
    resultados=[]
    for l in range(6):
        menor_t=min(matriz[l])
        list.append(resultados,menor_t)
    melhor_t=min(resultados)
    linha=list.index(resultados,melhor_t)
    corredor=linha+1
    volta=list.index(matriz[linha],melhor_t)+1


    return resultados