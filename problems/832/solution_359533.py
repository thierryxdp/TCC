def eh_quadrada(matriz):
    x=0
    y=0
    for a in matriz:
        x+=1
        for b in a:
            y+=1
            if x==y:
                return True