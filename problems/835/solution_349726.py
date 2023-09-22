def melhor_volta(matriz):
    """retorna uma tupla contendo resultados de melhor a pior tempo
    list -> tuple"""
    r=()
    for c in matriz:
        q=0
        l=[]
        for v in c:
            l.append(v)
        r=r+(min(l), )
    return r