def eh_quadrada(matriz):
    x=0
    y=0
    for i in matriz:
        if x==y:
            return False
        elif y==x:
            return False
    else:
        return True