def melhor_volta(matriz):
    '''
    funcAO QUE RECEBE UMA MATRIZ COM OS TEMPOS DE CADA CORREDOR
    EM 10 VOLTAS E RETORNA DE QUEM FOI A MELHOR VOLTA E O TEMPO
    MATRIZ -> TUPLA
    '''
    
    tupla = (0,0,0)
    
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < tupla:
                tupla = (i+1,matriz[i][j],j+1)
        return tupla