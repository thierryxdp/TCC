def filtra_pares(x):
    a = x[0] 
    b = x[1] 
    c = x[2]
    d = x[3]
    tupla_final = ()
    if a%2 == 0:
        tupla_final=tupla_final + (w,)
    if b%2 == 0:
        tupla_final= tupla_final + (x,)
    if c % 2 == 0:
        tupla_final= tupla_final + (y,)
    if d % 2 ==0:
        tupla_final= tupla_final + (z,)

    return tupla_final