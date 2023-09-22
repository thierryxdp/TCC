def eh_quadrada(matriz):
    """Retorne se a matriz é quadrada"""
    c=0
    d=0
    for i in range(len(matriz)):
        c=c+1
        for x in range(len(matriz[i])):
            if c==0:
                d=d+1
                return True
            elif c==d:
                return True
            elif len(matriz) == 1 and len(matriz[0]) ==0:
                return True
            else:
                return False