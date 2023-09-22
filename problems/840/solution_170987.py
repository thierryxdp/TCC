def bolos(a,b,c):
    from math import floor
    n_farinha = a / 2
    b_farinha = floor(n_farinha)
    n_ovos = b / 3
    b_ovos = floor(n_ovos)
    n_leite = c / 5
    b_leite = floor(n_leite)
    n_bolos = min(b_farinha, b_ovos, b_leite)
    return n_bolos