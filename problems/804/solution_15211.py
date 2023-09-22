filtra_pares(a):
    w = a[0] 
    x = a[1] 
    y = a[2]
    z = a[3]
    tupla_final = ()
    if w%2==0:
        tupla_final=tupla_final + (w,)
    if x%2 == 0:
        tupla_final= tupla_final + (x,)
    if y % 2 == 0:
        tupla_final= tupla_final + (y,)
    if z % 2 ==0:
        tupla_final= tupla_final + (z,)

    return tupla_final