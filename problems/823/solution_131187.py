def faltante(listafaltante):
    N = (len(listafaltante) + 1)
    listacompleta = list(range(1,N+1))
    indice = 0
    
    while list.count(listafaltante,listacompleta[indice]) != 0:
        indice += 1
    return listacompleta[indice]