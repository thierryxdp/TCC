def melhor_volta(matriz):
    ''' '''
    resultado=()
    tempo=min(matriz)
    volta=matriz.index(tempo)
    for i in matriz:
        for j in i:
            resultado+=(matriz[tempo],tempo,volta)
    return resultado