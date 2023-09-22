def num_bolos(A,B,C):
    """Retorna a quantidade de bolos conforme a quantidade minima de ingredientes necessaria"""
    far = A//2
    ovos = B//3
    sopa = C//5
    return min(far,ovos,sopa)