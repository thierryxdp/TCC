def melhor_volta(matriz):
    '''funcao que dado uma matriz 6X10 retorna
    quem fez a melhor volta e qual o tempo;
    list -> '''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    melhores_voltas = []
    
    for i in range(linhas):
        for j in range(colunas):
            melhores_voltas = melhores_voltas + min([matriz[i][j]])
    volta = min(melhores_voltas)
    return (volta, )