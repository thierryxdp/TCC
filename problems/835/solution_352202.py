def melhor_volta(matriz):
    lista=[]
    for i in range(len(matriz)):
        linha=[]
        for j in range(len(matriz[0])):
            linha.append(matriz[i][j])
            melhor=min(linha)
        lista.append(melhor)
        melhor2=min(lista)
        if melhor2 in linha:
            corrida=linha.index(melhor2)
            corredor=lista.index(melhor2)
    return (melhor2,corredor+1,corrida+1)