def melhor_volta(matriz):
    '''Recebe uma matriz 6x10 com os tempos em segundos e retorna uma tupla contendo quem fez a melhor volta, em qual volta e qual o tempo;
    list -> tup'''
    melhores_voltas=[]
    for linha in matriz:
        list.append(melhores_voltas,min(linha))
    tempo=min(melhores_voltas)
    corredor=list.index(melhores_voltas,tempo)
    volta=list.index(matriz[corredor],tempo)
    return (corredor+1,tempo,volta+1)