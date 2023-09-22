def melhor_volta(matriz):
    '''função que recebe como entrada uma matriz 6x10 com os tempos dos corredores e retorna de quem foi a melhor volta:list->tuple'''
    x=[0,0,0]
    lista_x = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(lista_x,matriz[i][j])
    
    m = min(lista_x)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz [i][j] == m:
                x[0] = i+1
                x[1] = matriz[i][j]
                x[2] = j +1