def faltante(L):
    ''' '''
    ordenada = L.copy()
    ordenada.sort()
    listaTeste = list(range(1,ordenada[-1] + 1))
    indice = 0
    while listaTeste[indice] in L:
            indice += 1
    return listaTeste[indice]