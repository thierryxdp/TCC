def melhor_volta(matriz):
    '''Essa função dada uma matriz contendo o tempo dos corredores em cada volta, 
    retorna uma tupla contendo a informação de quem deu a melhor volta, em qual tempo e em que volta,
    list->tuple'''
    linha=range(6)
    coluna=range(10)
    for linha in len(matriz):
        for coluna in len(matriz[linha]):
        if linha in coluna:
    return min(linha)