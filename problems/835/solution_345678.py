def melhor_volta(matriz):
    ''' '''
    listaminimos = []
    for m in range(len(matriz)):
        listaminimos = listaminimos + [min(matriz[m])]
    qualtempo = min(listaminimos)
    quemfoi = list.index(listaminimos,qualtempo)
    qualvolta = list.index(matriz[quemfoi],qualtempo)
    return (quemfoi + 1,qualtempo,qualvolta + 1)