def melhor_volta(matriz):
    '''funcao que dado uma matriz 6X10 retorna
    de quem foi a melhor volta,qual o tempo;
    e em que volta; list -> int,int,int'''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    melhores_voltas = []
    volta = 0
    
    for i in range(linhas):
        for j in range(colunas):
            melhores_voltas = melhores_voltas + [min([matriz[i][j]])]
    volta = volta + min(melhores_voltas)
    return (0,volta,0)