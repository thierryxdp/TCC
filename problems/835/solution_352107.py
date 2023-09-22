def melhor_volta(matriz):
    '''
    funcAO QUE RECEBE UMA MATRIZ COM OS TEMPOS DE CADA CORREDOR
    EM 10 VOLTAS E RETORNA DE QUEM FOI A MELHOR VOLTA E O TEMPO
    MATRIZ -> TUPLA
    '''
    
    tupla = (7,1000,11)
    i = 0
    j = 0
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1)
                i += 1
                j += 1
        return tupla