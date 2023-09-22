def melhor_volta(matriz):
    '''Função que, considerando 10 voltas de 6 corredores, retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta;list->tuple'''
    numerosmenores=[]
    contador=0
    for i in matriz:
        list.append(numerosmenores,min(i))
    minimo=min(numerosmenores)
    quem=list.index(numerosmenores,minimo)+1
    volta=list.index(matriz[quem],minimo)
    return quem,minimo,volta