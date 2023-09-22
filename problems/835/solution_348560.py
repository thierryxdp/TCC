#Q4

def melhor_volta(matriz):
    '''dado uma matriz 6 x 10, a função retorna de quem foi a melhor volta,
    com qual o melhor tempo e em que volta;
    list-> tuple'''
    t = float('inf')
    c = 0
    v = 0 
    for i in range(0,6):
        for j in range(0,10):
            if matriz[i][j] < t:
                
                t = matriz[i][j]
                c = i+1
                v = j+1
    return (c,t,v)