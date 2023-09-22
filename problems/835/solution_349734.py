def melhor_volta(matriz):
    """retorna uma tupla contendo resultados de melhor a pior tempo
    list -> tuple"""
    r=()
    l=[]
    i=0
    for c in matriz:
        q=0
        for v in c:
            l.append(v)
    tempo=min(l)
    for c in matriz:
        q=0
        i+=1
        for v in c:
            if v==tempo:
                corredor=i
                corrida=c.index(v)+1
    r=(corredor,tempo,corrida)
    return r