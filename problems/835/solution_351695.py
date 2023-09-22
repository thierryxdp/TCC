def melhor_volta(matriz):
    ''' funcao recebe uma matriz 6x10 e informa quem foi a melhro volta
    qual tempo e quem que volta, lis-->tup'''
    time_min=[]
    for linha in matriz:
        list.appedn(time_min,min(linha))
        time_min_geral= min(time_min)
        corredor= list.index(time_min,time_min_total)+1
        for tempo in linha:
            if tempo==time_min_total:
                volta=list.index(linha,tempo)+1
    return (corredor,time_min_total,volta)