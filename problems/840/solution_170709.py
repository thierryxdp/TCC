def bolo(a,b,c):
    from math import floor
    if (a<2 or b<2 or c<5):
        return 0
    else:
        farinha = floor(a/2)
        ovos = floor(b/2)
        leite = floor(c/5)
        total_bolos = min(farinha, ovos, leite)
        return total_bolos