def media_matriz(matriz):
    z=0
    x=0
    for i in matriz:
        for h in i:
            x=x+1
            z=h+z
    k=z/x        
    return round(k,2)