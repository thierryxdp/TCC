def melhor_volta(matriz):
    ''' '''
    resultado=[]
    minimos=()
    for i in matriz:
        for j in i:
            minimos=minimos+(min(matriz))
    return (list.index(matriz,(min(minimos))),min(minimos))