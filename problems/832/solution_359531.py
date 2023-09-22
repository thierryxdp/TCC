def eh_quadrada(matriz):
    x=0
    y=0
    for a in matriz:
        for b in a:
            x+=1
        y+=1
            if x==y:
                return True