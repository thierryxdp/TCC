def bolos(A, B, C):
    lim_farinha = A // 2
    lim_ovos = B // 3
    lim_leite = C //5
    return min(lim_farinha, lim_ovos, lim_leite)