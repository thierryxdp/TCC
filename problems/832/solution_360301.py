def eh_quadrada(matriz):
    if len(matriz)==0:
        return True
    if len(matriz)%2!=0 or len(matriz[0])!= len(matriz[-1]) or len(matriz[0])<2:
        return False
    for x in matriz:
        for y in x:
            if y==0:
                return False
    else:
        return True