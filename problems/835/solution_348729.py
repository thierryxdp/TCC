def melhor_volta(matriz):
    volta=120
    kart=0
    y=[]
    for a in matriz:
        for b in a:
            if b<volta:
                volta = b
    return volta,y