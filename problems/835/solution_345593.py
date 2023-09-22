def melhor_volta(matriz):
    """ Função que recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta.
    	A função retorna uma tupla contendo de quem foi a melhor volta, com qual tempo e em que volta
        Todos os corredores possuem tempos diferentes
        list->tuple
     """
    
    mtempo = 9999
    volta = 0
    corredor = 0
    
    for i in range(0,6):
        for j in range(0,10):
            if matriz[i][j]<mtempo:
                mtempo = matriz[i][j]
                volta = j
                corredor = i
    return [corredor+1, mtempo, volta+1]