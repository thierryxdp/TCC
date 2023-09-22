def conta_numero(n:int,m:list)->int:
    x=0
    for i in len (matriz):
        for j in len(matriz[i]):
            if matriz[i][j]==n:
                x+=1
    return x