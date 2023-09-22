def melhor_volta(matriz):
    '''essa função calcula entre os corredores o que
    fez a melhor volta no melhor tempo;list->tuple'''
    lista=[]
    for linha in matriz:
        tempo=min(linha)
        lista.append(tempo)
    menortempo=min(lista)
    corredor=list.index(lista,menortempo) + 1
    for linha in matriz:
        for coluna in linha:
            if coluna==menortempo:
                volta = list.index(linha,menortempo)+1
    return (corredor,menortempo,volta)