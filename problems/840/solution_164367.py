def bolos(a,b,c):
    min_xicara = a//2
    min_ovo = b//3
    min_leite = c//5
    minimo = min(min_xicara,min_ovo)
    minimo = min(minimo,min_leite)
    return minimo