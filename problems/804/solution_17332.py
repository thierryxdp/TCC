def filtra_pares(w,x,y,z):
    tupla_par=tuple()
    if w % 2==0:
        return tupla_par+'w'
    elif x % 2==0:
        return tupla_par+'x'
    elif y % 2==0:
        return tupla_par+'y'
    elif z % 2==0:
        return tupla_par+'z'
    else:
        return tupla_par