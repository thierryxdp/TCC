def filtra_pares(w,x,y,z):
    '''filtra os números pares de uma tupla dados os elementos"w","x","y" e "z"'''
    tupla_par=tuple()
    if w % 2==0:
        tupla_par = tupla_par+tuple(w)
    if x % 2==0:
         tupla_par = tupla_par+tuple(x)
    if y % 2==0:
         tupla_par = tupla_par+tuple(y)
    if z % 2==0:
         tupla_par = tupla_par+tuple(z)
    return tupla_par