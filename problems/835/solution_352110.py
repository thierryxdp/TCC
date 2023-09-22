def melhor_volta(matriz):
    '''
    funcAO QUE RECEBE UMA MATRIZ COM OS TEMPOS DE CADA CORREDOR
    EM 10 VOLTAS E RETORNA DE QUEM FOI A MELHOR VOLTA E O TEMPO
    MATRIZ -> TUPLA
    '''
    
    tupla = (7,1000,11)
    comp = 0
    tempo = 0
    volta = 0
    
    for i in range(10):
        for j in range(6):
            if matriz[j][i] < matriz[j][i+1]:
                comp = j
                tempo = matriz[j][i]
                volta = j
            i += 1
            j += 1                
        return (comp,tempo,volta)