def eh_quadrada(matriz):
    x=0
    y=0
    if len(matriz)==0:
        return True
    for i in matriz:
        x+=1
        for j in i:
            y+=1
    if y/x==x:
        return True
    else:
        return False