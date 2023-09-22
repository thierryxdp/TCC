def melhor_volta(matriz):
    tempo=()
    for i in matriz:
        for j in i:
            tempo+=(j,)
    btempo= min(tempo)
    
    t=0
    maximo=()
    btempos=()
    for x in matriz[t]:
        maximo+=(x,)
        a=min(maximo)
        if x==1:
            btempos+=a
            t+=1
        
    return btempos