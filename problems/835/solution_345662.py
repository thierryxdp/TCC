def melhor_volta(matriz):
    """Determina o menor tempo dentre vários corredores em uma corrida"""
    tempos = []
    indexcorredor = []
    indexvolta = []
    m = len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elemento = matriz[i][j]
            list.append(tempos,elemento)
            list.append(indexcorredor,i)
            list.append(indexvolta,j)
    index = list.index(tempos,min(tempos))
    return (indexcorredor[index],min(tempos))