def melhor_volta(voltas):
    '''Retorna de quem foi a melhor volta de Kart, com qual tempo e em que volta
    matrix->tuple'''
    lin_melhor=0
    col_melhor=0
    lin=0
    col=0
    for lin in range(len(voltas)):
        menor_temp=min(voltas[lin])
        if menor_temp>voltas[lin][col]:
            lin_melhor=lin
            col_melhor=list.index(voltas[lin],menor_temp)
    
    return (lin_melhor+1,col_melhor+1,voltas[lin_melhor][col_melhor])