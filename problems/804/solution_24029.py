def filtra_pares(ina):
    tupla_par = ()
    if ina[0]%2 == 0:
        tupla_par = tupla_par + (ina[0],)
    if ina[1]%2 == 0:
        tupla_par = tupla_par + (ina[1],)
    if ina[2]%2 == 0:
        tupla_par = tupla_par + (ina[2],)
    if ina[3]%2 == 0:
        tupla_par = tupla_par + (ina[3],)
    return tupla_par