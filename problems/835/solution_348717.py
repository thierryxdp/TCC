def melhor_volta(matriz):
    volta=110
    kart=0
    y=[]
    for a in matriz:
        kart +=1
        for b in a:
            if b<volta:
                volta = b
                return [volta]