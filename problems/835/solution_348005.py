def melhor_volta(matriz):
    '''Função que retorna o melhor tempo, qual corredor e a melhor
       volta. Lista - > tuple'''
    volta = 0
    corredor = 0
    tempo = tempos[volta]
    for tempos in matriz:
        for j in range(len(tempos)):
            if tempos[j] < tempos[volta]:
                volta = j
            corredor = corredor + 1
            
            
    return (corredor,tempo,volta+1)