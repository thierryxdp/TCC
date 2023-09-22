def conta_numero(numero,matriz):
    """retorna o numero de vezes que um numero aparece na matriz
    int, list -> int"""
    t=0
    l=[]
    for n in matriz:
        l.append(n)
        for nu in n:
            if nu==numero:
                t+=1        
    return t