def eh_quadrada(matriz):
    x=0
    y=0
    for i in matriz:
        x+=1
        for j in i:
            y+=1
    if y/x==x or len(matriz)==0:
        return True
    else:
        return False