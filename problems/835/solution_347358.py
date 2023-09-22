def melhor_volta(matriz):
    '''Dada uma matriz representando os dados de cada volta de cada corredor, retorna uma tupla que informa de quem foi a melhor volta, qual foi seu tempo e em qual volta. list->tuple.'''
    aux = ()
    for i in range(0,6):
        for j in range(0,10):
            aux += matriz[i][j],
    for i in range(0,6):
        for j in range(0,10):
            if matriz[i][j] == min(aux):
                corredor = i+1
                volta = j+1
    return (corredor, min(aux), volta)