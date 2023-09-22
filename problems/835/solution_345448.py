def melhor_volta(matriz):
    '''função que recebe uma matriz com as 10 voltas de 6 corredores numerados de 1 a 6 e retorna quem fez a melhor 
    volta, em qual tempo e em que volta.
    list -> tuple'''
    
    melhores_voltas = []
    
    for i in range(len(matriz)):
        list.append(melhores_voltas, min(matriz[i]))
    corredor = list.index(melhores_voltas, min(melhores_voltas))
    identificador = list.index(matriz[corredor], min(melhores_voltas))
    
    return melhores_voltas, corredor, identificador