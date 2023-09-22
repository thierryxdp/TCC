def melhor_volta(matriz):
    """Função que recebe como entrada uma matriz 6x10 com os 
    tempos em segundos dos corredoresem cada volta. A função
    retorna uma tupla informando de quem foi o melhor tempo 
    de prova, com qual tempo e em que volta.
    matriz->tupla"""
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
    return (corredor+1,melhor2,corrida+1)