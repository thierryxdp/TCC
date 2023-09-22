def melhor_volta(matriz):
    ''' '''
    minimos = []
    for i in range(len(matriz)):
        minimos += [min(matriz[i])]
    competidor =list.index(minimos,min(minimos))
    voltas = list.index(matriz[competidor],min(minimos))
    return (competidor+1,min(minimos),voltas+1)