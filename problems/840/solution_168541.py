def bolos(A,B,C):
    """Funçao que calcule quantidade de bolos que João consegue fazer"""
    xicara_minimo= A//2
    ovos_minimo = B//3 
    sopaleite_minimo = C//5
    return min (xicara_minimo,ovos_minimo,sopaleite_minimo)