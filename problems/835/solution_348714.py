def melhor_volta(matriz):
    volta=110
    kart=0
    y=[]
    for a in matriz:
        for b in a:
            if b<volta:
                volta = b
                kart=a+1
    return kart and volta