def melhor_volta(matriz):
    tempo=()
    for i in matriz:
        for j in i:
            tempo+=(j,)
    btempo= min(tempo)
    
    t=0
    maximo=()
    btempos=()
    acu=0
    for x in matriz[t]:
        maximo+=(x,)
        a=min(maximo)
        acu+=1
        if acu==5:
            btempos+=(a,)
            t+=1
        
    return btempos