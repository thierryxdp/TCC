def melhor_volta(matriz):
    z=[]
    for i in matriz:
        z=[min(i)]+z
    melhor_tempo=min(z)
    for i in matriz:
        for h in i:
            if melhor_tempo==h:
                corredor=i
    return (corredor,melhor_tempo)