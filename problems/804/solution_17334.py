def filtra_pares(w,x,y,z):
    tupla_par=tuple()
    if w % 2==0:
        return tupla_par+tuple(w)
    elif x % 2==0:
        return tupla_par+tuple(x)
    elif y % 2==0:
        return tupla_par+tuple(y)
    elif z % 2==0:
        return tupla_par+tuple(z)
    else:
        return tupla_par