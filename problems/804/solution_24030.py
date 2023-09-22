def filtra_pares(uc):
    tupla_par = ()
    if uc[0]%2 == 0:
        tupla_par = tupla_par + (uc[0],)
    if uc[1]%2 == 0:
        tupla_par = tupla_par + (uc[1],)
    if uc[2]%2 == 0:
        tupla_par = tupla_par + (uc[2],)
    if uc[3]%2 == 0:
        tupla_par = tupla_par + (uc[3],)
    return tupla_par