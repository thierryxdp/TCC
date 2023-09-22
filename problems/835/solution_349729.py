def melhor_volta(matriz):
    """retorna uma tupla contendo resultados de melhor a pior tempo
    list -> tuple"""
    r=()
    l=[]
    for c in matriz:
        q=0
        for v in c:
            l.append(v)
    tempo=min(l)
    for c in matriz:
        q=0
        for v in c:
            if v==tempo:
                corredor=c
                corrida=list.index(tempo, v)
    r=(corredor,tempo,corrida)
    return r