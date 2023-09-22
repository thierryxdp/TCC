def melhor_volta(matriz):
    '''Dada uma matriz 6x10, na qual as linhas representam
    os tempos de cada piloto e as colunas são os tempos em si,
    retorna uma tupla informando de quem foi a melhor volta,
    com qual tempo e em que volta; list[list[int]] -> tuple[int]'''
    final = []
    corredores = list(range(1,7))
    melhores_voltas = []
    i=0
    for linha in matriz:
        melhores_voltas.append(min(matriz[i]))
        i+=1
    final.append(melhores_voltas.index(min(melhores_voltas))+1)
    final.append(min(melhores_voltas))
    final.append(matriz.index(min(matriz[final[0]][final[1]])))
    return tuple(final)