def melhor_volta(matriz):
    '''retorna uma tupla dizendo de quem foi a melhor volta, o tempo e em qual volta
    matriz -> tupla'''
    temp=(1,0,1)
    for a in range(6):
        for b in range(10):
            if matriz[a][b]<temp[0]:
                temp = a+1,matriz[a][b],b+1
            return temp