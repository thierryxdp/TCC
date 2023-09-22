def melhor_volta(matriz):
    '''essa função calcula entre os corredores o que
    fez a melhor volta no melhor tempo;list->tuple'''
    lista=[]
    for linha in matriz:
        tempo=min(linha)
        lista.append(tempo)
    menortempo=min(lista)
    corredor=list.index(lista,menortempo) + 1
    volta=matriz[corredor-1][list.index(matriz[corredor-1],menortempo)]
    return (corredor,menortempo,volta)