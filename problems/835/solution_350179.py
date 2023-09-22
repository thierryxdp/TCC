def melhor_volta(matriz):
    '''Recebe uma matriz com 10 voltas para cada um de 6 corredores e retorna uma tupla com
    quem fez a melhor volta da prova, alem do tempo e do numero da volta.
    list->tuple'''
    menores=[]
    for linha in matriz:
        menores=menores+[min(linha)]
    menor_tempo=min(menores)
    corredor=list.index(menores,menor_tempo)
    volta=list.index(matriz[corredor],menor_tempo)
    return (corredor+1,menor_tempo,volta+1)