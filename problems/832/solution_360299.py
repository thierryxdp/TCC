def eh_quadrada(matriz):
    if len(matriz)%2!=0 or len(matriz[0])!= len(matriz[-1]):
        return False
    for x in matriz:
        for y in x:
            if y==0:
                return False
    else:
        return True