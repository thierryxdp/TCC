def eh_quadrada(matriz):
    i=0
    for num in matriz:
        if num!=0:
            i=1
    if i==0:
        return False
    elif i==1:
        return True