def melhor_volta(matriz):
    '''
    funcAO QUE RECEBE UMA MATRIZ COM OS TEMPOS DE CADA CORREDOR
    EM 10 VOLTAS E RETORNA DE QUEM FOI A MELHOR VOLTA E O TEMPO
    MATRIZ -> TUPLA
    '''
    
    tupla = (7,1000,11)
    
    for i in range(10):
        for j in range(6):
            if matriz[j][i] < tupla[1]:
                tupla = (j+1,matriz[j][i],i+1)
                
        return tupla