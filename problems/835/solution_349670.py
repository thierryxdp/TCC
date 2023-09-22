def melhor_volta(m):
    '''
    A função retorna a melhor volta de uma corrida de 
    6 corredores e dez voltas
    matriz --> tuple
    '''
    l = []
    for i in range(len(m)):
        l += [min(m[i], list.index(m[i], min(m[i])))]
    return list.index(l, min(l)), min(l), l[list.index(l, min(l)) + 1]