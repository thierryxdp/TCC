def melhor_volta(matriz):
    listacorridas = []
    qualvolta = 1
    for corredor in matriz:
        menor = min(corredor)
        listacorridas.append(menor)
    indice = listacorridas.index(min(listacorridas))
    for corrida in corredor:
        if corrida != min(listacorridas):
            qualvolta += 1
    return (indice+1,listacorridas[indice],qualvolta)