def bolos(a,b,c):
    " " "Calcula e retorna a quantidade minima de bolos que da pra fazer com a,b e c; int, int -> float ; int, int -> float; int, int -> float " " "
    min_xicara = a//2
    min_ovo = b//3
    min_leite = c//5
    minimo = min(min_xicara,min_ovo)
    minimo = min(minimo,min_leite)
    return minimo