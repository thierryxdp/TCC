def melhor_volta(matriz):
    z=[]
    y=0
    for i in matriz:
        z=[min(i)]+z
    melhor_tempo=min(z)
    for i in matriz:
        y=y+1
        for h in i:
            if melhor_tempo==h:
                corredor=y
    return (corredor,melhor_tempo)