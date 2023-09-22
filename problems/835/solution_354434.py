def melhor_volta(matriz):
    '''essa função calcula entre os corredores o que
    fez a melhor volta no melhor tempo;list->tuple'''
    lista=[]
    for linha in matriz:
        tempo=min(linha)
        lista.append(tempo)
    menortempo=min(lista)
    corredor=list.index(lista,menortempo)
    volta=list.index(matriz[corredor][list.index(matriz[corredor],menortempo)])
    return (corredor,menortempo,volta)