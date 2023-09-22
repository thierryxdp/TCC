def melhor_volta(matriz):
    z=[]
    y=0
    k=0
    for i in matriz:
        z=[min(i)]+z
    melhor_tempo=min(z)
    for i in matriz:
        y=y+1
        for h in i:
            if melhor_tempo==h:
                corredor=y
    for i in matriz:
        for h in i:
            k=k+1
            if melhor_tempo==h:
                rapido=k-(corredor-1)*10            
    return (corredor,melhor_tempo,rapido)