def melhor_volta (matriz):
    '''Função que recebe uma matriz 6x10 e nos retorna um tupla com a melhor volta
    matrix -> tuple'''

    '''[t t t t t t t t t t]
       [t t t t t t t t t t]
       [t t t t t t t t t t]
       [t t t t t t t t t t]
       [t t t t t t t t t t]
       [t t t t t t t t t t]6x10'''

    corredores = len(matriz) #linhas
    voltas = len(matriz[0]) #colunas

    menor_tempo = matriz[0][0]

    for volta in range(corredores):
        #Acessa cada linha da matriz
        for tempo in range(voltas):
            #Acessa cada elemento de cada linha (coluna)
            if menor_tempo >= matriz[volta][tempo]:
                menor_tempo = matriz[volta][tempo]
                
                melhor_corredor = volta+1 #Melhor volta (corredor) = linha de menor_tempo
                qual_volta = tempo+1 #Em que volta (volta) = coluna de menor_tempo

    return (melhor_corredor, menor_tempo, qual_volta)