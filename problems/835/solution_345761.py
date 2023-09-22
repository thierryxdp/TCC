def melhor_volta(matriz):
    '''A função recebe uma matriz de entrada contendo o desenvolvimento dos corredores numa pista de kart e retorna uma tupla informando
    de quem foi a melhor volta, com qual tempo e em que volta.list->tuple'''
    listaminimos = []
    for m in range(len(matriz)):
        listaminimos = listaminimos + [min(matriz[m])]
    qualtempo = min(listaminimos)
    quemfoi = list.index(listaminimos,qualtempo)
    qualvolta = list.index(matriz[quemfoi],qualtempo)
    return (quemfoi + 1,qualtempo,qualvolta + 1)